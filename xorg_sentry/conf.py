# Configuration for xorg_sentry.

from sentry.conf.server import *


# Cleanup social_auth-related stuff
# =================================

EXCLUDED_APPS = ('djcelery', 'kombu.transport.django', 'social_auth', 'django_social_auth_trello')
INSTALLED_APPS = tuple(app for app in INSTALLED_APPS if app not in EXCLUDED_APPS)

TEMPLATE_CONTEXT_PROCESSORS = tuple(
    tcp for tcp in TEMPLATE_CONTEXT_PROCESSORS if 'social_auth' not in tcp)


# Reading password
# ================

import os.path

CONF_ROOT = os.path.dirname(__file__)

def get_password(filename):
    with open(os.path.join(CONF_ROOT, 'private', filename)) as f:
        return f.readline().strip()


# Actual configuration
# ====================

AUTHENTICATION_BACKENDS = (
    #'sentry.utils.auth.EmailAuthBackend',
    'django_authgroupex.auth.AuthGroupeXBackend',
)

DATABASES = {
    'default': {
        # You can swap out the engine for MySQL easily by changing this value
        # to ``django.db.backends.mysql`` or to PostgreSQL with
        # ``django.db.backends.postgresql_psycopg2``
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sentry',
        'USER': 'sentry',
        'PASSWORD': get_password('mysql_key'),
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django_authgroupex',
    'xorg_sentry',
) + INSTALLED_APPS

ROOT_URLCONF = 'xorg_sentry.urls'

SENTRY_KEY = get_password('secret_key')

# Set this to false to require authentication
SENTRY_PUBLIC = True

# You should configure the absolute URI to Sentry. It will attempt to guess it if you don't
# but proxies may interfere with this.
# SENTRY_URL_PREFIX = 'http://sentry.example.com'  # No trailing slash!
SENTRY_URL_PREFIX = 'https://errors.polytechnique.org'

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    # 'worker_class': 'gevent',
}

# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False


AUTHGROUPEX_KEY = get_password('authgroupex_key')
AUTHGROUPEX_SUPERADMIN_PERMS = ('admin',)
AUTHGROUPEX_STAFF_PERMS = ('admin',)
AUTHGROUPEX_RETURN_URL = 'https://errors.polytechnique.org/xorgauth/'
AUTHGROUPEX_FIELDS = ('username', 'firstname', 'lastname', 'perms')
