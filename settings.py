# Minimal django settings to run tests

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': './sqlite3.db',                      # Or path to database file if using sqlite3.
    }
}

SECRET_KEY = 'alksjdf93jqpijsdaklfjq;3lejqklejlakefjas'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django_seo_js.middleware.HashBangMiddleware',
    'django_seo_js.middleware.UserAgentMiddleware',
)

# ROOT_URLCONF = 'djproject.urls'

# Python dotted path to the WSGI application used by Django's runserver.
# WSGI_APPLICATION = 'djproject.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'django_seo_js'
    }
}