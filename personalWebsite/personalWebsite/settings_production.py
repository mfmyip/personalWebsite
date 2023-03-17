"""
Django settings for personalWebsite project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import json
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# Get logins from env variable
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
POSTGRESQL_USER = os.getenv('POSTGRESQL_USER')
POSTGRESQL_PASSWORD = os.getenv('POSTGRESQL_PASSWORD')

# SECURITY WARNING: keep the secret key used in production secret!
if not (SECRET_KEY and POSTGRESQL_USER and POSTGRESQL_PASSWORD):
    with open( Path('personalWebsite') / 'secrets.json', 'r') as f:
        data = json.load(f)
        SECRET_KEY = data.get('SECRET_KEY')
        POSTGRESQL_USER = data.get('POSTGRESQL').get('USER')
        POSTGRESQL_PASSWORD = data.get('POSTGRESQL').get('PASSWORD')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
LOCAL_DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'django-app-dev3.us-east-2.elasticbeanstalk.com', '172.31.34.76', 'murphyyip.info', 'www.murphyyip.info', '192.168.50.28']

## (replace the string below with your own site URL):
CSRF_TRUSTED_ORIGINS = ['django-app-dev3.us-east-2.elasticbeanstalk.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projects',
    'contact',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

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

# Simplified static file serving.
# https://pypi.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'personalWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["personalWebsite/templates/"],
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

WSGI_APPLICATION = 'personalWebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebdb',
        'USER': POSTGRESQL_USER,
        'PASSWORD': POSTGRESQL_PASSWORD,
        'HOST': 'awseb-e-8wkzi5t33e-stack-awsebrdsdatabase-bogibrz5e8nj.czffkad3dr3v.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR /'static'
#STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]

# FOR EMAILS
if LOCAL_DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django_ses.SESBackend'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    if (not AWS_ACCESS_KEY_ID) or (not AWS_SECRET_ACCESS_KEY):
        raise ValueError('AWS KEYS NOT FOUND')
    AWS_SES_REGION_NAME = 'us-east-2' #(ex: us-east-2)
    AWS_SES_REGION_ENDPOINT ='email.us-east-2.amazonaws.com' #(ex: email.us-east-2.amazonaws.com)


# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR , "media")

# print(MEDIA_ROOT, MEDIA_URL)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'