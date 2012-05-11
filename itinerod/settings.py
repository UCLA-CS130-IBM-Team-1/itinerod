# Django settings for itinerod project.
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_DIR = os.path.dirname(__file__)

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),

)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'itinerod',                      # Or path to database file if using sqlite3.
        'USER': 'itinerod',                      # Not used with sqlite3.
        'PASSWORD': 'meEH!EsF',                  # Not used with sqlite3.
        'HOST': 'mysql.itinerod.dreamhosters.com',                      # Set to empty string for localhost. Not used with sqlite3
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, '../media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6c$fl3%&1u9eg!osb%l!u_@)v1roeis#o^xm@6fkqac_3grp2w'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'itinerod.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, '../templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',

    'itinerod',
    # Openid stuff
    'django_openid_auth',
    'registration',
    # Database migrations
    'south',
)

AUTHENTICATION_BACKENDS = (
    'auth.GoogleBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/google/login/'
LOGIN_REDIRECT_URL = '/profile/'
LOGOUT_URL = '/google/logout/'
OPENID_SSO_SERVER_URL = 'https://www.google.com/accounts/o8/id'

EMAIL_HOST = 'mail.ucla.edu'
EMAIL_HOST_USER = 'stefanwoj89'
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = 'star10'
DEFAULT_FROM_EMAIL = 'stefanwoj89@ucla.edu'
ACCOUNT_ACTIVATION_DAYS = 2

try:
  from local_settings import *
except ImportError:
  pass
