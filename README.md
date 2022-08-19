# trial-app

This is a trial app. <br /> 
A recipe app that has create, read, update, and delete funtionality <br />

This project was created with:
* python
* django
* django_rest_framework
* htmx
* alpine.js
* sqlite

## You should have python 3.8 and up installed in your system to run this trial-app

## Clone this app
```
git clone https://github.com/yohi441/trial-app.git
```

## Navigate to the folder you clone

## Create virtual environment
```
python3 -m venv venv
```

## Activate virtual environment
```
source venv/bin/activate
```

## Install projects dependency using pip
```
pip install -r requirements.txt
```

## Run the app using manage.py
```
python manage.py runserver
```


# You can access the django built-in admin using this credentials
# admin url 127.0.0.1:8000/admin/
```
email: admin@email.com
password: adminpassword
```

# You can login to the app using this credentials
# or you can signup 
```
email: test@email.com
password: testpassword
```

## You can also use the API


## API endpoints 


| METHOD | URI | SEMANTICS |
| --- | --- | --- |
| GET | /api/ | Retrieve list of URL of recipe list |
| GET | /api/recipes/all/ | Retrieve list of all recipes of all users |
| GET | /api/recipe/detail/{id}/ | Retrieve a single recipe |
| GET | /api/recipe/list/ |  Retrieve a list of recipes of the user must provide basic authentication |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
METHOD           URI                           SEMANTICS

GET        /api/                     Retrieve list of URL of recipe list

GET        /api/recipes/all/         Retrieve list of all recipes of all users

GET        /api/recipe/detail/{id}/  Retrieve a single recipe

GET        /api/recipe/list/         Retrieve a list of recipes of the user
                                     must provide basic authentication

POST       /api/recipe/list/         Create a new recipe of the user
                                     must provide basic authentication

GET        /api/recipe/{id}/         Retrieve a single recipe of the user
                                     must provide basic authentication

PUT        /api/recipe/{id}/         Update an existing recipe of the user
                                     must provide basic authentication

DELETE     /api/recipe/{id}/         Delete an existing recipe of the user
                                     must provide basic authentication


