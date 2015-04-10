__author__ = 'brian'
"""
Django settings for paw_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import json
import os
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# STATIC_ROOT = os.path.join(BASE_DIR, "static")


DEBUG = False
TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = '/home/zalewski/paw_project/media'
MEDIA_URL = '/~paxson/media/'
STATIC_URL = '/~paxson/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets"),
)
# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, "paw_project", "secrets.json")) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# TEMPLATE_DEBUG = True
#
# ALLOWED_HOSTS = [
#     'localhost',
#     '.fgcu.edu',
#     '.fgcu.edu.',
#     '.satnet.fgcu.edu',
#     '.satnet.fgcu.edu.',
# ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_markdown',
    'poems',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'paw_project.urls'

WSGI_APPLICATION = 'paw_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)