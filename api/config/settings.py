import os
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

def env_list(some):
    if isinstance(some, list):
        return some
    else:
        return some.split(',')

def env_bool(some):
    if isinstance(some, bool):
        return some
    else:
        return bool(some)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", env.get_value("SECRET_KEY", str))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_bool(os.getenv("DEBUG", env.bool("DEBUG", default=False)))

ALLOWED_HOSTS = env_list(os.getenv("ALLOWED_HOSTS", env.list("ALLOWED_HOSTS")))

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_cleanup.apps.CleanupConfig",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",
    "rest_framework",
    "account.apps.AccountConfig",
    "apiv1.apps.Apiv1Config",
]

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
        "DIRS": [
            os.path.join(BASE_DIR, "templates")
        ],
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
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", env.get_value("DB_ENGINE", str)),
        "NAME": "vantan_store_db",
        "USER": os.getenv("DB_USER", env.get_value("DB_USER", str)),
        "PASSWORD": os.getenv("DB_PASSWORD", env.get_value("DB_PASSWORD", str)),
        "PORT": os.getenv("DB_PORT", env.get_value("DB_PORT", str)),
        "HOST": os.getenv("DB_HOST", env.get_value("DB_HOST", str)),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'vantan.store.noreply@gmail.com'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # send_mailのfromがNoneの場合自動で入る。
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", env.get_value("EMAIL_HOST_PASSWORD", str))

AUTH_USER_MODEL = 'account.AccountUser'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
