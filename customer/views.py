from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from.utils import send_sms

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        phone_number = instance.customer.phonenumber  
        message = f"Your order {instance.id} has been successfully placed!"

        if send_sms(phone_number, message):
            print("SMS sent successfully")
        else:
            print("Failed to send SMS")

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
    


class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
