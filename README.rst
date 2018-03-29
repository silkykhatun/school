**School** is a test project for courses:

* API endpoints available for user, course module.
* Fast, easy and high performance application with django.
* Highly customizeable with as few lines of code as possible for application developers.

===========================
Features
===========================
----------------------------------------
* Functionality as a django application
----------------------------------------
  - User signup/login feature. Loose coupled app, that can be taken out easily and use anywhere else.

---------------
* API endpoints
---------------
  - https://sleepy-woodland-56323.herokuapp.com/user/api-v1/users/ (To check the details of all available users)
  - https://sleepy-woodland-56323.herokuapp.com/user/api-v1/user/(?P<term>[-\w]+)/ (search user with name/email/username containing the term searched)
  - https://sleepy-woodland-56323.herokuapp.com/blog/api-v1/enroll (POST: To enroll in a course)
  - https://sleepy-woodland-56323.herokuapp.com/blog/api-v1/quit (POST: To quit in a course)

===========================
Documentation
===========================
---------------------------------
Steps to Install the application
---------------------------------
- Create a virtualenvironment with python 3.6 and install all requirements.
- Create a database with any database technology you prefer and add the db details in the local_settings.py preferably in mysql.
- Save the local_settings.py in school/school directory.
- run *python manage.py migrate usermanager* to create db user table and the *python manage.py migrate* for other tables.
- run *python manage.py runserver* and you are ready to go.
- the logs are stored at log/ directory in main.log, you can have app wise more logs by adding more handlers in settings.

===========================
Demo
===========================

https://sleepy-woodland-56323.herokuapp.com

===========================
Technologies used
===========================
dj-database-url==0.5.0
Django==1.11
django-rest-framework==0.1.0
django-rest-framework-docs==0.1.7
django-rest-swagger==2.1.2
djangorestframework==3.7.7
ipython==6.2.1
psycopg2==2.7.4
psycopg2-binary==2.7.4
gunicorn