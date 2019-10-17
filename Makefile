.PHONY: all

all: install migrations cache static test coverage run

coverage:
	coverage run --source='.' manage.py test liaoey.apps
	coverage report -m

cache:
	python manage.py createcachetable

coverage-html:
	coverage html

docd:
	docker-compose up -d --build

docdown:
	docker-compose down -v

install:
	pip install -r requirements.txt

migrations:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver 0.0.0.0:8000

static:
	python manage.py collectstatic --noinput

test:
	python manage.py test liaoey.apps
