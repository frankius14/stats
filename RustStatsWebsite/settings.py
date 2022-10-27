"""
Django settings for RustStatsWebsite project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os, sys
from credentials import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# TODO: Generate a new key and place it in credentials.py
SECRET_KEY = django_secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if os.getenv('GAE_APPLICATION', None):
    ALLOWED_HOSTS = ["ruststats.gg"]
else:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

SITE_ID = 1  # Sites framework, used for sitemap
SESSION_COOKIE_AGE = 15552000  # 6 months

# Application definition

INSTALLED_APPS = [
    'rust_stats',
    'social_django',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'RustStatsWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'rust_stats.context_processors.categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'RustStatsWebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


if os.getenv('GAE_APPLICATION', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': production_host,
            'USER': production_user,
            'PASSWORD': production_password,
            'NAME': production_name,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': local_host,
            'PORT': local_port,
            'PASSWORD': local_password,
            'NAME': local_name,
            'USER': local_user,
        },
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

if not 'test' in sys.argv:  # Disable logging during unit tests
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'basic': {
                'format': '{levelname}|{asctime}|{module}: {message}',
                'datefmt': '%Y-%m-%d %H:%M:%S',
                'style': '{',
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'basic'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'WARNING',
                'propagate': True
            },
            'rust_stats': {
                'handlers': ['console'],
                'level': 'WARNING',
            }
        },
    }

    
AUTHENTICATION_BACKENDS = (
    'social_core.backends.steam.SteamOpenId',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/my_profile'
SOCIAL_AUTH_STEAM_API_KEY = steam_api_key
# TODO: 
# Once migrated to Postgresql, enable this field 
# according to social-auth-app-django documentation
# https://python-social-auth.readthedocs.io/en/latest/configuration/django.html#database
# SOCIAL_AUTH_POSTGRES_JSONFIELD = True