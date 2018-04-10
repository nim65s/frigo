import os

PROJECT = 'frigo'
PROJECT_VERBOSE = PROJECT.capitalize()
SELF_MAIL = False
DOMAIN_NAME = os.environ.get('DOMAIN_NAME', 'local')
HOSTNAME = os.environ.get('ALLOWED_HOST', f'{PROJECT}.{DOMAIN_NAME}')
ALLOWED_HOSTS = [HOSTNAME]
ALLOWED_HOSTS += [f'www.{host}' for host in ALLOWED_HOSTS]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

EMAIL_USE_SSL = True
EMAIL_HOST = os.environ.get('EMAIL_HOST', f'smtp.{DOMAIN_NAME}')
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USER = os.environ.get('EMAIL_USER', 'majo')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 465)
EMAIL_FQDN = os.environ.get('EMAIL_FQDN', ALLOWED_HOSTS[0] if SELF_MAIL else DOMAIN_NAME)
EMAIL_HOST_USER = f'{EMAIL_USER}@{EMAIL_FQDN}'
SERVER_EMAIL = f'{EMAIL_USER}+{PROJECT}@{EMAIL_FQDN}'
DEFAULT_FROM_EMAIL = f'{PROJECT_VERBOSE} <{EMAIL_USER}@{EMAIL_FQDN}>'
EMAIL_BACKEND = 'django.core.mail.backends.%s' % ('filebased.EmailBackend' if DEBUG else 'smtp.EmailBackend')
EMAIL_SUBJECT_PREFIX = f'[{PROJECT_VERBOSE}] '

ADMINS = ((os.environ.get('ADMIN_NAME', f'{PROJECT_VERBOSE} webmaster'),
           os.environ.get('ADMIN_MAIL', f'webmaster@{DOMAIN_NAME}')),)
MANAGERS = ADMINS

INSTALLED_APPS = [
    PROJECT,
    'ndh',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_tables2',
    'bootstrap4',
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

ROOT_URLCONF = f'{PROJECT}.root_urls'

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

DB = os.environ.get('DB', 'db.sqlite3')
DATABASES = {
    'default': {
        'ENGINE': f'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, DB),
    }
}
if DB == 'postgres':
    DATABASES['default'].update(
        ENGINE='django.db.backends.postgresql',
        NAME=os.environ.get('POSTGRES_DB', DB),
        USER=os.environ.get('POSTGRES_USER', DB),
        HOST=os.environ.get('POSTGRES_HOST', DB),
        PASSWORD=os.environ['POSTGRES_PASSWORD'],
    )

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

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'fr-FR')
TIME_ZONE = os.environ.get('TIME_ZONE', 'Europe/Paris')
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = int(os.environ.get('SITE_ID', 1))

MEDIA_ROOT = '/srv/media/'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = '/srv/static/'
LOGIN_REDIRECT_URL = '/'

if os.environ.get('MEMCACHED', 'False').lower() == 'true':
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'memcached:11211',
        }
    }

if os.environ.get('RAVEN', 'False').lower() == 'true':
    INSTALLED_APPS.append('raven.contrib.django.raven_compat')
    RAVEN_CONFIG = {'dsn': os.environ['DSN']}

AUTHENTICATION_BACKENDS = ['yeouia.backends.YummyEmailOrUsernameInsensitiveAuth']
DJANGO_TABLES2_TEMPLATE = f'{PROJECT}/tables.html'
LOGIN_REDIRECT_URL = '/'
