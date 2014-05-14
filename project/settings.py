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
HTDOCS_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, '..', 'htdocs'))

# Files uploaded by users
MEDIA_ROOT = os.path.join(HTDOCS_ROOT, 'media')
MEDIA_URL = '/media/'

# Static files from apps
STATIC_ROOT = os.path.join(HTDOCS_ROOT, 'static')
STATIC_URL = '/static/'

# Use pgrunner to develop against PostgreSQL instead of sqlite?
PGRUNNER = False
# WARNING: DATABASES will be overwritten by pgrunner below, if PGRUNNER = True
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
if PGRUNNER:
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

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_pyscss.compressor.DjangoScssFilter'),
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
    'mezzanine.core.request.CurrentRequestMiddleware',
    'mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware',
    'mezzanine.pages.middleware.PageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "mezzanine.conf.context_processors.settings",
    "mezzanine.pages.context_processors.page"
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',

    'mezzanine.boot',
    'mezzanine.conf',
    'mezzanine.core',
    'mezzanine.generic',
    'mezzanine.pages',
    'filebrowser_safe',
    'grappelli_safe',

    'widgy',
    'widgy.contrib.page_builder',
    'widgy.contrib.form_builder',
    'widgy.contrib.widgy_mezzanine',

    # Must come after mezzanine, grappelli and widgy
    'django.contrib.admin',
    'django.contrib.admindocs',

    'filer',
    'easy_thumbnails',
    'compressor',
    'argonauts',
    'scss',
    'sorl.thumbnail',

    'south',

    # dev
    'django_extensions',
]
if PGRUNNER:
    INSTALLED_APPS.append('pgrunner')

# Settings for widgy
# See http://docs.wid.gy/en/latest/tutorials/widgy-mezzanine-tutorial.html
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
TESTING = False
GRAPPELLI_INSTALLED = True
# If you want mezzanine to use WidgyPage as the default page, you can add the
# following line to your settings file:
ADD_PAGE_ORDER = (
    'widgy_mezzanine.WidgyPage',
)
#WIDGY_MEZZANINE_PAGE_MODEL =
WIDGY_MEZZANINE_SITE = 'project.widgy_site.site'

ADMIN_MENU_ORDER = [
    ('Widgy', (
        'pages.Page',
        'page_builder.Callout',
        'form_builder.Form',
        ('Review queue', 'review_queue.ReviewedVersionCommit'),
    )),
]

# Hack needed for easy_thumbnails
SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}


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
