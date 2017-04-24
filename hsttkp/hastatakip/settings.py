# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

with open('/etc/secret') as f:
    SECRET_KEY = f.read().strip()

DEBUG = False

ALLOWED_HOSTS = [
    'hsttkp.zygns.com', 
    'hastatakip.zygns.com'
]

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'muayene.apps.MuayeneConfig',
    'hasta.apps.HastaConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions', 
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware', 
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hastatakip.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/templates/',
            PROJECT_PATH + '/templates/',    
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hastatakip.context.get_user',
                'hastatakip.context.get_week_month_year'
            ],
        },
    },
]

WSGI_APPLICATION = 'hastatakip.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hastatakip',
        'USER': 'hastatakip',
        'PASSWORD': 'hastatakip',
        'HOST': 'localhost',
        'PORT': '',
    },
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Turkey'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = [
    '%d/%m/%Y',    
    '%d/%m/%y',    
    '%d-%m-%Y',    
    '%d-%m-%y',    
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/staticfiles/' 
STATIC_ROOT = '/home/hastatakip/static'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'        
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles/'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/hastatakip/media'

caches = {
    'default': {
        'backend': 'django.core.cache.backends.memcached.memcachedcache',
        'location': 'hastatakip.zygns.com:11511'
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/hastatakip/logs/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True
        },
    },
}

try:
    from local_settings import *
except ImportError:
    print("No local_settings file!")
