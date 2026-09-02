"""
Settings specific to using this template in local containerized (principally in WSL within a cArmy Developer AVD)
"""

import os

from dotenv import load_dotenv

from ..base import *

load_dotenv()

DEBUG = True

ALLOWED_HOSTS = ["backend", "*"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-u8^#*!f@4%gpodaniz_7*x8vv^92d!5nccb_1-m!msjr9#lp*6"

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASS"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ["DB_PORT"],
    }
}
