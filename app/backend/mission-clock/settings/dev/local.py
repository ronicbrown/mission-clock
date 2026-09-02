"""
Settings specific to using this template in local development (principally in WSL within a cArmy Developer AVD)
"""

from ..base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "*", "backend"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-u8^#*!f@4%gpodaniz_7*x8vv^92d!5nccb_1-m!msjr9#lp*6"

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
