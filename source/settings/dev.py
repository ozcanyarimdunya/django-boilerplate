from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
INSTALLED_APPS += [
    'constance.backends.database',
]
