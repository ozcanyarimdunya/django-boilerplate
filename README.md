# Project

[![Build Status](https://travis-ci.org/ozcanyarimdunya/django-boilerplate.svg?branch=master)](https://travis-ci.org/ozcanyarimdunya/django-boilerplate)
[![Coverage Status](https://coveralls.io/repos/github/ozcanyarimdunya/django-boilerplate/badge.svg?branch=master)](https://coveralls.io/github/ozcanyarimdunya/django-boilerplate?branch=master)

**NOTE**: Change above badges with your own repository url.

> A boilerplate django project.

## Installation

1. Clone the repository.
   ```
   $ git clone https://github.com/ozcanyarimdunya/django-boilerplate.git myapp
   $ cd myapp/
   ```

2. Install the virtualenv package, create new virtual environment and activate it.
   ```
   $ pip install virtualenv
   $ virtualenv venv
   $ source venv/bin/activate
   ```

3. Install all dependencies and start application on [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
   ```
   $ make
   ```

4. To access admin panel, create a superuser and visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
   ```
   $ make superuser
   ```
    
## Running in docker

1. Make sure you have installed **docker** and **docker-compose**.
   ```
   $ make docd
   ```

2. To access admin panel, create a superuser in docker and visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
   ```
   $ docker exec -ti docker_webapp_1 make superuser
   ```
