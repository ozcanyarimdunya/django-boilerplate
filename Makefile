.PHONY: all

all: install migrations initial static test coverage run

coverage:
	coverage run --source='.' manage.py test source.apps
	coverage report -m

cache:
	python manage.py createcachetable

coverage-html:
	coverage html

docb:
	cd docker && docker-compose up --build

docd:
	cd docker && docker-compose up -d --build

docdown:
	cd docker && docker-compose down -v

documentation:
	cd docs && make html

install:
	pip install -r requirements.txt

initial:
	python manage.py loaddata source/initial.json

migrations:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver 127.0.0.1:8000

static:
	python manage.py collectstatic --noinput

test:
	python manage.py test source.apps
