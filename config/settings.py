from datetime import timedelta
import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", default=get_random_secret_key())
DEBUG = os.getenv("DEBUG", default="False") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default="127.0.0.1").split(", ")
CSRF_TRUSTED_ORIGINS = os.getenv("TRUSTED_ORIGINS", default="").split(", ")
# CORS_ALLOWED_ORIGINS = os.getenv("TRUSTED_ORIGINS", default="").split(", ")
CORS_ALLOW_ALL_ORIGINS = True

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "djoser",
    "drf_spectacular",
    "corsheaders",
]

LOCAL_APPS = [
    "apps.users.apps.UsersConfig",
    "apps.specialists.apps.SpecialistsConfig",
    "apps.api.apps.ApiConfig",
    "apps.core.apps.CoreConfig",
    "apps.events.apps.EventsConfig",
    "apps.attributes.apps.AttributesConfig",
]

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_NAME", default="postgres"),
        "USER": os.getenv("POSTGRES_USER", default="postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="postgres"),
        "HOST": os.getenv("POSTGRES_HOST", default="db"),
        "PORT": os.getenv("POSTGRES_PORT", default=5432),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.CustomUser"

REST_FRAMEWORK = {
    # "DEFAULT_PERMISSION_CLASSES": (
    #     "rest_framework.permissions.IsAuthenticated",
    # ),
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DATE_FORMAT": "%d.%m.%Y",
    "DATETIME_FORMAT": "%d.%m.%Y %H:%M",
    "DATETIME_INPUT_FORMATS": ["%d.%m.%Y %H:%M"],
    "DATETIME_FORMAT": "%d.%m.%Y %H:%M",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "TBD. Команда 7-Eleven",
    "DESCRIPTION": "TBD",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX": "/api/v1/",
    "SWAGGER_UI_DIST": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.3",
}

# DJOSER = {
#     "SERIALIZERS": {
#         "user_create": "apps.api.v1.users.serializers.CreateUserSerializer",
#         "current_user": "apps.api.v1.users.serializers.MeUserSerializer",
#     },
#     "HIDE_USERS": True,
# }

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1 * 24 * 5),  # пока пишем код
    "REFRESH_TOKEN_LIFETIME": timedelta(weeks=10),
    "AUTH_HEADER_TYPES": ("JWT",),
}

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", default="admin@admin.admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", default="Password-123")
