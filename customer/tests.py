from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Customer, Order

class CustomerAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer_data = {'name': 'Bridgit', 'phonenumber': '0716588562', 'code': '001'}
        self.customer = Customer.objects.create(**self.customer_data)
        self.customer_url = reverse('customer-list-create')

    def test_create_customer(self):
        response = self.client.post(self.customer_url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)  

    def test_get_customers(self):
        response = self.client.get(self.customer_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_customer(self):
        url = reverse('customer-detail', kwargs={'pk': self.customer.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.customer.name)

    def test_update_customer(self):
        url = reverse('customer-detail', kwargs={'pk': self.customer.id})
        updated_data = {'name': 'Bridgit ', 'phonenumber': '0716588562', 'code': '002'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.customer.name, 'Bridgit')

    def test_delete_customer(self):
        url = reverse('customer-detail', kwargs={'pk': self.customer.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)

class OrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name='James', phonenumber='0716588562', code='001')
        self.order_data = {'customer': self.customer.id, 'item': 'Phone', 'amount': 99.99}
        self.order = Order.objects.create(customer=self.customer, item='Laptop', amount=99.99)
        self.order_url = reverse('order-list-create')

    def test_create_order(self):
        response = self.client.post(self.order_url, self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)  

    def test_get_orders(self):
        response = self.client.get(self.order_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_order(self):
        url = reverse('order-detail', kwargs={'pk': self.order.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['item'], self.order.item)

    def test_update_order(self):
        url = reverse('order-detail', kwargs={'pk': self.order.id})
        updated_data = {'customer': self.customer.id, 'item': 'Fridge', 'amount': 199.99}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.item, 'Fridge')

    def test_delete_order(self):
        url = reverse('order-detail', kwargs={'pk': self.order.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)
