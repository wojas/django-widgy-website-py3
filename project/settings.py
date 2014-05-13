import os, sys, socket

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Always symlink for this project
if 'collectstatic' in sys.argv and not ('-l' in sys.argv or '--link' in sys.argv):
    print("NOTE: forcing --link for collectstatic")
    sys.argv.append('--link')

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_DIRNAME = os.path.abspath(os.path.dirname(__file__))
DIRNAME = os.path.abspath(os.path.join(PROJECT_DIRNAME, '..'))

RUNNING_RUNSERVER = 'runserver' in sys.argv
DEBUG = RUNNING_RUNSERVER or os.getenv('DEBUG', False) or socket.gethostname()=='dev3'
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = not DEBUG
PROFILING = DEBUG

# If you want to change it in local_settings, it is not enough to just override
# this one: you also have to copy all the variables that use it.
HTDOCS_ROOT = os.path.join(PROJECT_ROOT, '..', '..', 'htdocs')

# Files uploaded by users
MEDIA_ROOT = os.path.join(HTDOCS_ROOT, 'media')
MEDIA_URL = '/media/'

# Static files from apps
STATIC_ROOT = os.path.join(HTDOCS_ROOT, 'static')
STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': '',
        'PORT': '',
        'NAME': os.path.join(DIRNAME, 'dev.db'),
        'USER': '',
        'PASSWORD': '',

    }
}

#try:
#    from postgresdevdb.settings import *
#except ImportError:
#    # Assume this is a production machine
#    pass
import pgrunner
pgrunner.settings(locals())

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


def get_secret_key(path):
    """Get the SECRET_KEY from a file, and creates it if needed"""
    from django.core.exceptions import SuspiciousOperation
    path = os.path.expanduser(path)
    if os.path.exists(path):
        with open(path, 'r') as f:
            key = f.read().strip()
    else:
        import django.utils.crypto
        chars = ''.join(chr(x) for x in range(33, 127))
        key = django.utils.crypto.get_random_string(100, chars)
        print("NOTE: creating new SECRET_KEY and writing to {}".format(path))
        with open(path, 'w') as f:
            f.write(key)
    if len(key) < 50:
        raise SuspiciousOperation("Secret key too short: {}".format(path))
    return key

# WARNING: if running on multiple servers, make sure they have the same key!
SECRET_KEY = get_secret_key(os.path.join(PROJECT_ROOT, 'secret_key'))


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
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'south',

    # dev
    'pgrunner',
    'django_extensions',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
