<h1 align="center">Menu</h1>

<p align="center">
  
<img src="https://img.shields.io/badge/python-v3.9-blue">

<img src="https://img.shields.io/badge/django-4.1.7-green">
 
</p>

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/belekabbasuulu/tz_project.git
$ cd tz_project
```

DOCKER:
```sh
docker-compose up
```

LOCAL:

Create a virtual environment to install dependencies in and activate it:

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:

```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ python manage.py createsuperuser
```

Finally:
```sh
(venv)$ python manage.py runserver
```