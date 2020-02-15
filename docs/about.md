# Project Structure

Project tree 

    .
    ├── db.sqlite3
    ├── docker
    │   ├── docker-compose.yml
    │   ├── entrypoint.sh
    │   ├── nginx
    │   │   ├── default.conf
    │   │   └── Dockerfile
    │   ├── start.sh
    │   └── webapp
    │       └── Dockerfile
    ├── docs
    │   ├── about.md
    │   └── index.md
    ├── Makefile
    ├── manage.py
    ├── mkdocs.yml
    ├── README.md
    ├── requirements.txt
    ├── source
    │   ├── apps
    │   │   ├── common
    │   │   │   ├── admin.py
    │   │   │   ├── apps.py
    │   │   │   ├── __init__.py
    │   │   │   ├── migrations
    │   │   │   │   └── __init__.py
    │   │   │   ├── models.py
    │   │   │   ├── tests.py
    │   │   │   ├── urls.py
    │   │   │   └── views.py
    │   │   └── __init__.py
    │   ├── assets
    │   │   ├── static
    │   │   └── static-dev
    │   │       └── local
    │   ├── contrib
    │   │   ├── __init__.py
    │   │   ├── tests
    │   │   │   ├── __init__.py
    │   │   │   └── test_utils.py
    │   │   └── utils.py
    │   ├── __init__.py
    │   ├── media
    │   ├── settings
    │   │   ├── base.py
    │   │   ├── dev.py
    │   │   ├── __init__.py
    │   │   └── prod.py
    │   ├── templates
    │   │   └── index.html
    │   ├── urls.py
    │   └── wsgi.py
    └── venv
    
    17 directories, 36 files
