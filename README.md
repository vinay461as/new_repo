# Django application
This is a small Django application with Member and ActivityPeriod models, it consist
- A custom management command to populate the database with some dummy data 
- An API to serve that data in the json format.

# Install Required Packages
The project was built and tested with Django 3.x version.The Django project need some Python package to install
```
pip install Django
pip install djangorestframework
pip install django-faker
```

# Running the Application
Before running the application we need to create the needed DB tables:
```
python manage.py makemigrations
python manage.py migrate
 ```
Now run the server
```
python manage.py runserver
```
To access the applications, go to the URL http://localhost:8000/

# Populate the database with some dummy data
To create dummy data use the below code:
```
python manage.py createmember
```
This command create 3 member in one go

# Serve that data in the json
To server the data in the json formate, go to the local URL http://localhost:8000/api/member

live server link http://djapppro.pythonanywhere.com/api
