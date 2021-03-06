"""
Django settings for sergi project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["cci.gov.tm", "www.cci.gov.tm", "95.85.122.57"]

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'sergi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                # 'django.core.mail.backends.console.EmailBackend'
            ],
        },
    },
]

WSGI_APPLICATION = 'sergi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tppdb',
        'USER': 'dbuser',
        'PASSWORD': 'google123',
        'HOST': 'localhost',
        'PORT': '',
    }
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

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'Asia/Ashgabat'

USE_I18N = True

USE_L10N = True

USE_TZ = True


def gettext(s): return s

# NEW_LANG_INFO = {
#     'tm': {
#        'bidi': True,
#        'code': 'tm',
#        'name': 'Turkmen',
#        'name_local': 'Turkmen',
#     },
# }


LANGUAGES = (
    ('ru', gettext('Russia')),
    ('en', gettext('English')),
    ('tk', gettext('Turkmen')),
)

# DEFAULT_FROM_EMAIL = ['conference@cci.gov.tm']
# DEFAULT_FROM_EMAIL = 'admin@mysite.com'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_HOST = 'imap.cci.gov.tm'
SERVER_EMAIL = 'conference@cci.gov.tm'  #
EMAIL_HOST_USER = 'conference@cci.gov.tm'  #
EMAIL_HOST_PASSWORD = 'Mailcon99!'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = "/home/projects/static/"
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

# if DEBUG:
#    STATIC_ROOT = os.path.join(BASE_DIR, '/static')
# else:
#    STATIC_ROOT = os.path.join(BASE_DIR, '/static')


# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = "/home/projects/media/"
MEDIA_URL = "/media/"

CKEDITOR_UPLOAD_PATH = "uploads/"
