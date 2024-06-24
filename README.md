`Overview`

This project is a simple web service that manages customers and orders. It includes a REST API for creating and retrieving customers and orders
and SMS notifications using Africa’s Talking SMS gateway.

`Steps`

git clone: https://github.com/AmakoveBridgit/CustomerService.git
cd CustomerOrdersService
cd orderservice

`Set up virtual environment`

python3 -m venv env
source env/bin/activate

`Install dependencies`

pip install -r requirements.txt

`Makemigrations`

python3 manage.py migrate

`Runserver`

python3 manage.py runserver



