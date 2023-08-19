Meta Backend Capstone

This is a capstone project for the Meta Back-End Development course

# Virtual Enviornment Commands
virtualenv venv 
source venv/bin/activate

# Pip install requirement file
pip3 install -r requirements.txt
# create a django project
django-admin startproject littlelemon
# run development server
cd littlelemon
python3 manage.py runserver
# create a django app 
python3 manage.py startapp restaurant
# Pip install SQL Database
pip3 install mysqlclient

# Creating the Database
create database littlelemon;
use littlelemon;
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'lemon@789!';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'admin'@'localhost';
python3 manage.py migrate 
python3 manage.py makemigrations

# Create admin superuser
python manage.py createsuperuser
#username: admin
#email: admin@littlelemon.com
#password: lemon@789!


GET in http://localhost:8000/api/menu/1

{
    "id": 1,
    "title": "Pizza",
    "price": "15.00",
    "inventory": 100
}

GET in http://localhost:8000/api/menu

Get all menus
POST http://localhost:8000/api/menu/

[
    {
        "id": 1,
        "title": "Pizza",
        "price": "15.00",
        "inventory": 100
    },
    {
        "id": 2,
        "title": "Pasta",
        "price": "20.00",
        "inventory": 50
    },
    {
        "id": 3,
        "title": "Carrot Cake",
        "price": "10.00",
        "inventory": 30
    }
]

GET in http://localhost:8000/api/booking/tables

[
    {
        "id": 1,
        "name": "Booking 1",
        "number_of_guests": 2,
        "booking_date": "2023-08-17T20:45:00Z"
    }
]

POST http://localhost:8000/api/api-token-auth/

{
    "token": "22846dabc22e55f086a19169d26c5f62c801f1cc"
}
Add authorization to the endpoints, so you have to send a header in the request with the Authorization title: Token [VALUE]

pip install djoser
navigate to http://127.0.0.1:8000/auth/token/login/ to get the token

user: "admin" 
password: "lemon@789!"
use http://127.0.0.1:8000/auth/token/logout/ to logout with the token in the header

Testing
python manage.py test
GRANT ALL PRIVILEGES ON `test_littlelemon`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
To execute the available unittests, please open the Visual Studio terminal and enter the following command: python manage.py test tests/. Please ensure that you have activated the virtual environment and navigated into the 'littlelemon' directory prior to running the unit-tests command.

Utilize this path to verify that the web application is serving static HTML content, inclusive of images and styling. /restaurant

For testing, you can make use of the following API endpoints with Insomnia or Postman clients. Alternatively, feel free to explore them through your browser of choice.

DJOSER endpoint, for instance, to perform a POST request and register a new user. /auth/users/

To log in and obtain an authentication token. /api-token-auth/

To log in using the DJOSER endpoint. /auth/token/login

Menu items /api/menu/ /api/menu/{menuItemId}

Table reservations /api/booking/tables/ /api/booking/tables/{bookingId}
