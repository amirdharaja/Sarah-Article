import os

from dotenv import load_dotenv
from pathlib import Path




env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('AUTH_SECRET_KEY')
SALT = os.getenv('SALT')
HASHER = os.getenv('HASHER')
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')



DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps',
]

AUTH_USER_MODEL = 'apps.Login'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ARTICLE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

MAILER_EMAIL_BACKEND = os.getenv('MAILER_EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = EMAIL_USERNAME
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_USE_TLS = True

WSGI_APPLICATION = 'ARTICLE.wsgi.application'

DATABASES = {

    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME' : os.getenv('DB_NAME'),
        'HOST': os.getenv('DB_HOST'),
        'PORT' : os.getenv('DB_PORT'),
        'USER' : os.getenv('DB_USERNAME'),
        'PASSWORD' : os.getenv('DB_PASSWORD'),
    },
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'images/')
MEDIA_URL = '/images/'

LOGOUT_REDIRECT = "home.html"
