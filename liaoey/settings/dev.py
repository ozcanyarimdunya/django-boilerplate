from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 123,
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
