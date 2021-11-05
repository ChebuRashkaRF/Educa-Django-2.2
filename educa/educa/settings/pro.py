from .base import *


DEBUG = False

ADMINS = (
    ('Antonoi M', '*****@gmail.com'),
)

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '*****',
        'USER': '*****',
        'PASSWORD': '*****',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
