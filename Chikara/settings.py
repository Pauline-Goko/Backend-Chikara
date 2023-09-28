"""
Django settings for Chikara project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url
from django.conf import settings
import django_heroku





BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


 




STATIC_URL = '/static/'  # Updated URL path

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Build paths inside the project like this: BASE_DIR / 'subdir'.


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2ctt&onfno5&co-l5osdc_w_lp@6xnfqnyb6lmpy1m==dpzeqc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'vehicles',
    'limits',
    'user',
    'phonenumber_field',
    'rest_framework.authtoken',
    'emissionsdata',
    'carbon_credits',
    'drf_yasg',
 

]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]
SESSION_ENGINE = "django.contrib.sessions.backends.db"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]
ROOT_URLCONF = 'Chikara.urls'
AUTH_USER_MODEL = 'user.User'
REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication']}

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
            ],
        },
    },
]

WSGI_APPLICATION = 'Chikara.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# DATABASES = {'default': dj_database_url.config(default=os.environ. get('DATABASE_URL'))}                                           
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chikara_app',
        'USER': 'chikara',
        'PASSWORD': 'chikara_pass',
        'HOST': 'localhost',
        'PORT': '',
    }
}
# export DATABASE_URL=postgres://chikara:chikara_pass@localhost:5432/chikara_app


MEDIA_ROOT = os.path.join(BASE_DIR, 'user_images')
MEDIA_URL = '/user_images/'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


django_heroku.settings(locals())
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field



