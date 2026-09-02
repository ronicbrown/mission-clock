"""
Settings specific to deploying this template in AI2C's Expedition 0 using a PostgreSQL Flexible Server
"""

import os

from ..base import *

DEBUG = True

ALLOWED_HOSTS = ["ai.army.mil"]

# Ensure you add a SECRET_KEY value to the environment of the deployed container!
SECRET_KEY = os.environ["SECRET_KEY"]

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
