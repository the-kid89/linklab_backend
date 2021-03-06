"""
Django settings for linklab project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import raven

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_*kimvidv(^*ddl2p9)iy=9=v3upkhu4w4ufvspc0pcbf7+fzi'

# SECURITY WARNING: don't run with debug turned on in production!
prod = os.environ.get('PROD', False)
if prod:
    DEBUG = False
else:
    DEBUG = True

if prod:
    ALLOWED_HOSTS = [
        'www.linklabs.site',
        'linklabs.site',
        'www.linklab.site',
        'linklab.site',
    ]
else:
    ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitch',
    'raven.contrib.django.raven_compat',
    'rest_framework',
    'user_profile',
]

SITE_ID = 2

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'linklab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'linklab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation    'allauth.socialaccount.providers.twitch',
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + STATIC_URL

ACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_PROVIDERS = {
    "twitch": {"SCOPE": ["user_read"]},
}
SOCIALACCOUNT_AUTO_SIGNUP = True

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', '')
GOOGLE_CHANNEL_API = (
    'https://www.googleapis.com/youtube/v3/channels?'
    'part=snippet%2CcontentDetails&'
    'forUsername={user}&key={YOUR_API_KEY}'
)
GOOGLE_PLAYLIST_API = (
   'https://www.googleapis.com/youtube/v3/playlistItems'
   '?playlistId={playlist_id}'
   '&maxResults=6&part=snippet&' 
   'key={YOUR_API_KEY}'
)

TWITCH_CLIENT_ID = os.environ.get('TWITCH_CLIENT_ID', '')
TWITCH_VIDEO_API = 'https://api.twitch.tv/helix/videos?user_id={user_id}'

RAVEN_CONFIG = {
    'dsn': 'https://f34ccc7fd60a4eac827c12c96f92dec6:3314af3441994b26b1e7142c16658933@sentry.io/1260826',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}
