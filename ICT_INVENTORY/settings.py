"""
Django settings for ICT_INVENTORY project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f2t(0v59^1-&8*jmr&e2)7oivi4)3-k%1v-)(nlvbb4@$%j808'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

    'order.apps.OrderConfig',

    'fifthfloor.apps.FifthfloorConfig',

    'stockin.apps.StockinConfig',

    'groundfloor.apps.GroundfloorConfig',

    'eighthfloor.apps.EighthfloorConfig',

    'faulty.apps.FaultyConfig',

    'scanners.apps.ScannersConfig',

    'messagingboard.apps.MessagingboardConfig',

    'tenthfloordataentry.apps.TenthfloordataentryConfig',

    'fourthfloorwingA.apps.FourthfloorwingaConfig',

    'landregistration.apps.LandregistrationConfig',

    'thirdfloor.apps.ThirdfloorConfig',

    'bankinghall.apps.BankinghallConfig',

    # add new app seventhfloor
    'seventhfloor.apps.SeventhfloorConfig',
     # add the new land_admin app
    'land_admin.apps.LandAdminConfig',

     # add our new users app
    'users.apps.UsersConfig',

     # 3rd party app
    'crispy_forms',
    'django.contrib.postgres',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'ICT_INVENTORY.urls'

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

WSGI_APPLICATION = 'ICT_INVENTORY.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'timothy',
        'PASSWORD': 'timothy',
        'HOST' : '127.0.0.1',
        'PORT' : '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# configuration of telling django to use our custom user model rather than the built-in
AUTH_USER_MODEL = 'users.CustomUser'

# route for logging-in and logging-out users
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
