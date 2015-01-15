"""
Django settings for mcexam project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
1
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#udaj!(^2-!hhvni4-d^4v!fq8aecw671j61%0&!e-v9b_#$d0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'base',
    'exams',
    'users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'base.middleware.TimeZoneMiddleware',
)

ROOT_URLCONF = 'mcexam.urls'

WSGI_APPLICATION = 'mcexam.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'base', 'templates'),
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'base', 'static'),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

SITE_ID = 1
AUTH_USER_MODEL = 'users.Member'
LOGIN_REDIRECT_URL = 'users:login'
LOGIN_URL = 'users:login'

AUTHENTICATION_BACKENDS = (
    'users.backends.MemberAuthBackend',
)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER='sh44zzz@gmail.com'
EMAIL_HOST_PASSWORD='idontforgetonce'
EMAIL_USE_TLS= True
EMAIL_SENDER = 'sh44zzz@gmail.com'

"""
#Heroku settings
import dj_database_url
DATABASES["default"] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

DEBUG = False

TEMPLATE_DEBUG = False
"""