"""
🔧 Django Base Settings – `base.py`

This module defines the **base configuration** for the Django project.
It includes all settings that are shared across development and production environments.

This file should not be modified per environment. Instead, extend it using separate
`dev.py` or `prod.py` files that import from this one.

────────────────────────────────────────────────
📚 Contents
────────────────────────────────────────────────
- Installed applications (Django, third-party, local apps)
- Middleware stack
- Template engine
- Django REST Framework with JWT
- Custom user model configuration
- Celery for asynchronous task scheduling
- Email backend via SMTP
- Logging configuration
- CORS headers for frontend communication
- Internationalization & static/media files
- Jazzmin admin theme customization

────────────────────────────────────────────────
📁 File Hierarchy Usage
────────────────────────────────────────────────
- base.py → shared/common settings
- dev.py → development-specific overrides
- prod.py → production-specific secure overrides

────────────────────────────────────────────────
⚠️ Notes
────────────────────────────────────────────────
- Do not commit secrets or `.env` to version control.
- Keep `DEBUG=False` in production.
- Always restrict `ALLOWED_HOSTS` in production settings.
"""

import os
from pathlib import Path
from datetime import timedelta
from celery.schedules import crontab
from dotenv import load_dotenv

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load environment variables from .env file
load_dotenv(BASE_DIR / ".env")

# ─────────────────────────────────────────────
# 🔐 Basic Security and Environment
# ─────────────────────────────────────────────

SECRET_KEY = os.getenv("SECRET_KEY", "fallback-key")
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = []

# ─────────────────────────────────────────────
# 👤 Custom User Model
# ─────────────────────────────────────────────
AUTH_USER_MODEL = "users.CustomUser"

# ─────────────────────────────────────────────
# 📦 Installed Applications
# ─────────────────────────────────────────────

# Core Django applications
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

# Third-party libraries
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "corsheaders",
    "celery",
    "redis",
    "jazzmin",
]

# Local project apps
LOCAL_APPS = [
    "apps.ads",
    "apps.feedback",
    "apps.inventory",
    "apps.menu",
    "apps.orders",
    "apps.reports",
    "apps.tables",
    "apps.users",
]

# Combine all app groups into a single list
INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

# ─────────────────────────────────────────────
# ⚙️ Middleware Configuration
# ─────────────────────────────────────────────
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

# ─────────────────────────────────────────────
# 🖼️ Template Engine Configuration
# ─────────────────────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # You can add custom template folders here
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"

# ─────────────────────────────────────────────
# 🔐 Authentication and REST API Settings
# ─────────────────────────────────────────────
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# JWT token lifespan and authentication settings
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

# ─────────────────────────────────────────────
# 🔑 Password Validators
# ─────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ─────────────────────────────────────────────
# 🌍 Internationalization & Localization
# ─────────────────────────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Baku"
USE_I18N = True
USE_TZ = True

# ─────────────────────────────────────────────
# 🗂️ Static & Media Files
# ─────────────────────────────────────────────
STATIC_URL = "static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ─────────────────────────────────────────────
# ⏱️ Celery Configuration (Redis Backend)
# ─────────────────────────────────────────────
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Baku'

# Scheduled tasks
CELERY_BEAT_SCHEDULE = {
    'send_email_task_every_day': {
        'task': 'apps.orders.tasks.send_email_task',
        'schedule': crontab(minute=0, hour=9),  # Every day at 09:00 AM
        'args': ('Daily Report', 'This is your daily email reminder.', ['recipient@example.com']),
    },
}

# ─────────────────────────────────────────────
# 📬 Email Configuration (SMTP)
# ─────────────────────────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

# ─────────────────────────────────────────────
# 🌐 CORS Configuration
# ─────────────────────────────────────────────
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://your-frontend-domain.com",
]

CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
    'accept',
    'origin',
]

CORS_ALLOW_CREDENTIALS = True
CORS_PREFLIGHT_MAX_AGE = 86400

# ─────────────────────────────────────────────
# 📝 Logging Configuration
# ─────────────────────────────────────────────
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{asctime} {levelname} {name} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "logs", "django.log"),
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

# ─────────────────────────────────────────────
# 🎨 Jazzmin Admin Theme Configuration
# ─────────────────────────────────────────────
JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": "darkly",
    "dark_mode": True,
    "navbar_small_text": True,
    "footer_small_text": True,
    "footer_copyright": "Your Company Name",
}
