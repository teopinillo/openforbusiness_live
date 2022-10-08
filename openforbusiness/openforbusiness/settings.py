"""
Django settings for openforbusiness project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import appsecrets as appsecrets

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = appsecrets.SECRET_KEY


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
AUTH_USER_MODEL = 'users.CustomUser'

# Application definition

INSTALLED_APPS = [   
    ##user app
    'users.apps.UsersConfig',
    'crispy_forms',
    'sites.apps.SitesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'openforbusiness',    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'login_required.middleware.LoginRequiredMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'openforbusiness.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'openforbusiness.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': appsecrets.DATABASE_NAME,
        'USER': appsecrets.DATABASE_ADMIN,
        'PASSWORD': appsecrets.DATABASE_ADMIN_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIR = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join (os.path.dirname(BASE_DIR), 'static')
MEDIA_ROOT = os.path.join (STATIC_ROOT, 'images')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_FROM_EMAIL = 'teopinillo@pm.me'

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

"""
https://learndjango.com/tutorials/django-password-reset-tutorial
SMTP Server
setup a way to deliver, or at least fake deliver, our email messages.
In the real-world you would integrate with an email service like MailGun or SendGrid. 
For development purposes Django lets us store emails either in the console or as a file. 
We'll choose the latter and store all sent emails in a folder called sent_emails in our project directory.
"""
# USE 1 OR 2
# ---- 1 ----
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))
# ---- 2 ----
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
########################## collage email id #####################
EMAIL_HOST_USER= appsecrets.MY_EMAIL
EMAIL_HOST_PASSWOD= appsecrets.MY_EMAIL_PASSWORD


CRISPY_TEMPLATE_PACK = 'bootstrap4'




