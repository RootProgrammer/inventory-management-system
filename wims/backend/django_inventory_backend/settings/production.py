from .base import *
import dj_database_url

DEBUG = False
DATABASES['default'] = dj_database_url.config(default=config('DATABASE_URL'))
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=lambda v: [s.strip() for s in v.split(',')])


# Modify your secret key for added security:
# SECRET_KEY = 'YOUR_PRODUCTION_SECRET_KEY'


"""
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourproductiondomain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prod_db',
        'USER': 'prod_user',
        'PASSWORD': 'prod_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Plus any other production-specific settings

"""