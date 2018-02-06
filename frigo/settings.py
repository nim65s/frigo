from os import environ
from os.path import abspath, dirname, join

PROJECT = 'frigo'
PROJECT_VERBOSE = PROJECT.capitalize()
SELF_MAIL = False
NAMESPACE = environ.get('NAMESPACE', 'totheweb.fr')
ALLOWED_HOSTS = [environ.get('ALLOWED_HOST', f'{PROJECT}.{NAMESPACE}')]
ALLOWED_HOSTS += [f'www.{host}' for host in ALLOWED_HOSTS]

BASE_DIR = dirname(dirname(abspath(__file__)))

SECRET_KEY = environ['SECRET_KEY']
DEBUG = environ.get('DEBUG', 'False').lower() == 'true'

EMAIL_USE_SSL = True
EMAIL_HOST = environ.get('EMAIL_HOST', f'smtp.{NAMESPACE}')
EMAIL_HOST_PASSWORD = environ['EMAIL_HOST_PASSWORD']
EMAIL_USER = environ.get('EMAIL_USER', 'majo')
EMAIL_PORT = environ.get('EMAIL_PORT', 465)
EMAIL_FQDN = environ.get('EMAIL_FQDN', ALLOWED_HOSTS[0] if SELF_MAIL else NAMESPACE)
EMAIL_HOST_USER = f'{EMAIL_USER}@{EMAIL_FQDN}'
SERVER_EMAIL = f'{EMAIL_USER}+{PROJECT}@{EMAIL_FQDN}'
DEFAULT_FROM_EMAIL = f'{PROJECT_VERBOSE} <{EMAIL_USER}@{EMAIL_FQDN}>'
EMAIL_BACKEND = 'django.core.mail.backends.%s' % ('filebased.EmailBackend' if DEBUG else 'smtp.EmailBackend')
EMAIL_SUBJECT_PREFIX = f'[{PROJECT_VERBOSE}] '

ADMINS = ((environ.get('ADMIN_NAME', f'{PROJECT_VERBOSE} webmaster'),
           environ.get('ADMIN_MAIL', f'webmaster+{PROJECT}@{NAMESPACE}')),)
MANAGERS = ADMINS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_tables2',
    'bootstrap3',
    'ndh',
    PROJECT,
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

ROOT_URLCONF = f'{PROJECT}.urls'

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

WSGI_APPLICATION = f'{PROJECT}.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = environ.get('LANGUAGE_CODE', 'fr-FR')
TIME_ZONE = environ.get('TIME_ZONE', 'Europe/Paris')
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = int(environ.get('SITE_ID', 1))

MEDIA_ROOT = '/srv/media/'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = '/srv/static/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    },
}

AUTHENTICATION_BACKENDS = ['yeouia.backends.YummyEmailOrUsernameInsensitiveAuth']
DJANGO_TABLES2_TEMPLATE = f'{PROJECT}/tables.html'
