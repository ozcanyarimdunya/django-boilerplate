#!/usr/bin/env bash

echo "... Applying Django migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable

echo "... Applying Django collect static"
python manage.py collectstatic --noinput --clear

echo "... Starting Django"
exec gunicorn liaoey.wsgi -b 0.0.0.0:8000 --reload