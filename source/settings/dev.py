from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'source': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
INSTALLED_APPS += [
    'constance.backends.database',
]
