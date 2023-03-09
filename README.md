# mini-site-api
The purpose of this project is to provide a standard REST JSON-API that would allow a mobile application or a full frontend website to display a mini site.

> This project is a Django 4 based app. soon I will do the same exercise with a clean-archi or Hexagonal architecture


# Installation 
* clone the project : `git@github.com:kdakhli/django-rest-mysql.git`

* inside the project folder run : `docker-compose pull` then `docker-compose up -d`

* run this command in order to update the database schema : `docker exec -it -u root django-rest-mysql_web_1 python manage.py migrate  --run-syncdb`

* now since the database is ready , we can add some data fixtures : `docker exec -it -u root django-rest-mysql_web_1 python manage.py init_local_dev`

* Now go to http://localhost:8000/admin to use the admin interface and go to http://localhost:8000/api to use the API

* Access to the database with Adminer : http://localhost:8080/?server=db&username=root&db=my-app-db

====> Enjoy :) 

# Testing 
* I haven't taken the test yet.

