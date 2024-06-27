"""
Django's settings for hube project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
CORS_ALLOW_ALL_ORIGINS = True
# Application definition

DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
]

LOCAL_APPS = [
    "user_app",
    "lecture_app",
    "task_app",
    "submission_app",
    "main_app",
    "tags_app"
]

THIRD_PARTY_APPS = [
    "compressor",  # new
    "drf_spectacular",
    "rest_framework.authtoken",
    "rest_framework_simplejwt.token_blacklist",
    "djoser",
    "rest_framework",
    "corsheaders",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_DB"),
        "USER": env.str("POSTGRES_USER"),
        "PASSWORD": env.str("POSTGRES_PASSWORD"),
        "HOST": env.str("POSTGRES_HOST"),
        "PORT": env.str("POSTGRES_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",

]

# Media files storage
MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Set auth User model
AUTH_USER_MODEL = "user_app.User"

# Compressor config
# Documentation at https://flowbite.com/docs/getting-started/django/

COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

# Djoser settings

DJOSER = {
    "TOKEN_MODEL": None,  # We use only JWT
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": False,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": False,
    "SEND_CONFIRMATION_EMAIL": False,
    "SET_USERNAME_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_URL": "reset_password/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "username/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": False,  # In future impl
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
}

# DRF settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",

    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

if DEBUG:
    REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"].append(
        "rest_framework.authentication.BasicAuthentication"
    )

# DRF-SPECTACULAR settings
SPECTACULAR_SETTINGS = {
    "SCHEMA_PATH_PREFIX": "/api",
}

# Jazzmin settings
JAZZMIN_SETTINGS = {
    "hide_apps": [
        "token_blacklist",
        "auth",
        "authtoken"]
}

# Logging settings
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        # Send all messages to console
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "loggers": {
        # This is the "catch all" logger
        "": {
            "handlers": [
                "console",
            ],
            "level": "DEBUG",
            "propagate": False,
        },
    },
    "formatters": {
        "default": {
            "format": "[{asctime}] {name} {levelname} {module} {message}",
            "style": "{",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        }
    },
}

# Celery Configuration
RABBITMQ_HOST = env.str("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_PORT = env.str("RABBITMQ_PORT", "5672")
RABBITMQ_DEFAULT_USER = env.str("RABBITMQ_DEFAULT_USER", "rmuser")
RABBITMQ_DEFAULT_PASS = env.str("RABBITMQ_DEFAULT_PASS", "rmpassword")
RABBITMQ_URL = f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@{RABBITMQ_HOST}:{RABBITMQ_PORT}"
RABBITMQ_BACKEND_URL = f"rpc://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@{RABBITMQ_HOST}:{RABBITMQ_PORT}"

CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", RABBITMQ_URL)
CELERY_RESULT_BACKEND = env.str(
    "CELERY_BROKER_BACKEND", RABBITMQ_BACKEND_URL
)
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# Chat gpt configuration
OPENAI_API_KEY = env.str("OPENAI_API_KEY")
OPENAI_USER_PROMPT = env.str("OPENAI_USER_PROMPT", "НАПИШИ СЛОВАМИ ЧТО МОЖНО ИСПРАВИТЬ В ЭТОМ КОДЕ")
OPENAI_SYSTEM_PROMPT = env.str("OPENAI_SYSTEM_PROMPT", "Представь что ты преподаватель по программированию")
OPENAI_MODEL = env.str("OPENAI_MODEL", "gpt-3.5")
SAVE_PROMPT = env.bool("SAVE_PROMPT", default=False)

# Giga chat configuration
GIGACHAT_API_KEY = env.str("GIGACHAT_API_KEY",
                           "M2IxNGU4NWItMDczMC00YTc2LWIzYzAtOTkyZDRiNjQ0MDhkOmVlNjlmMjRiLWFkMDQtNDMxNy05NWQ2LWI3OGE0MGUxZDRjMg==")
SSL_SERTS = env.bool("SSL_SERTS", default=False)