import os
from collections import OrderedDict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'si*52#bq8#88qafliumhv#@yge6edq&vn2moy2l4e=t)7b61kc'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party application
    'constance',

    # custom application
    'source.apps.common.apps.CommonConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'source.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'constance.context_processors.config',  # constance
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'source.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets', 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets', 'static-dev', 'local')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SITE_HEADER = "Project"

# constance settings
CONSTANCE_CONFIG = OrderedDict([
    ('SITE_TITLE', ('', 'Website title')),
    ('SITE_NAME', ('', 'Website name')),
    ('SITE_AUTHOR', ('', 'Website author')),
    ('SITE_DESCRIPTION', ('', 'Website description')),
    ('SITE_FOOTER_TEXT', ('', 'Website footer text')),
    ('SITE_FACEBOOK_URL', ('', 'Website Facebook url')),
    ('SITE_TWITTER_URL', ('', 'Website Twitter url')),
    ('SITE_INSTAGRAM_URL', ('', 'Website Instagram url')),
])

CONSTANCE_CONFIG_FIELDSETS = OrderedDict([
    ('Site Settings', (
        'SITE_TITLE',
        'SITE_NAME',
        'SITE_FOOTER_TEXT',
        'SITE_AUTHOR',
        'SITE_DESCRIPTION',
    )),
    ('Social Links', (
        'SITE_FACEBOOK_URL',
        'SITE_TWITTER_URL',
        'SITE_INSTAGRAM_URL',
    )),
])
