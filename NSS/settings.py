"""
Django settings for NSS project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&a%k#g+bsqh$zvfy0jg7$e6s_1+^fizy0=z@t-m%z(s&=q8(@i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0:8000', '127.0.0.1', '192.168.29.132', 'treeasurenss.siesgst.ac.in', 'treeasurenss.herokuapp.com']


# SENDGRID_API_KEY = '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'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'treeasurenss@gmail.com'
EMAIL_HOST_PASSWORD = 'treeasure@nss123'

# Application definition

INSTALLED_APPS = [
    'information.apps.InformationConfig',
    'maps.apps.MapsConfig',
    'schedule.apps.ScheduleConfig',
    'home.apps.HomeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NSS.urls'

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

WSGI_APPLICATION = 'NSS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# mysql://bf07c1db527b49:3caf1e6d@us-cdbr-east-03.cleardb.com/heroku_7c0e58c726f0b71?reconnect=true

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'plantation',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_7c0e58c726f0b71',
        'USER': 'bf07c1db527b49',
        'PASSWORD': '3caf1e6d',
        'HOST': 'us-cdbr-east-03.cleardb.com',
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
# print(STATIC_ROOT)
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # location for server to store files
# MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
# print(MEDIA_ROOT)
MEDIA_URL = '/media/'

# MEDIA_URL = 'http://treeasurenss.heroku.com/media/'
# MEDIA_ROOT = '/home/admin/webapps/static_media'
