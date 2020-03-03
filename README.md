Locations is a Countries and Cities small app. Written with django and used vue.js for the frontend (via CDN).

# Please follow the process below

You may use Python 3.7 (optional)

- after installing python 3.7
- pipenv --python 3.7

1. Clone this repository (use `git clone ...`)

## setting up a development environment

2. start an environment with requirements
   e.g. pipenv install -r locations/requirements.txt

   base pip files are: django and django-rest-framework
   however requirements file includes much more.

## migrating the already defined models and creating the super user

3. python manage.py migrate

## super user should be created before the dummy data be loaded!

4. python manage.py createsuperuser

## loading dummy data

5. python manage.py loaddata data.json

P.S:

1. you may follow the process as the ordering defined or there may be problems with user related data
2. There is a problems.md file
