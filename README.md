ronicbrown@CAZVW0FVAA3-59K:~/message-board/app$ cd ~/message-board/app

sed -n '1,220p' \
backend/message-board/settings/dev/local_postgres.py
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

CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "http://172.19.160.96",
    "http://localhost:5173",
]


CSRF_COOKIE_HTTPONLY = True
ronicbrown@CAZVW0FVAA3-59K:~/message-board/app$ docker compose --env-file .env --profile all exec -T backend python3 - <<'PY'T backend python3 - <<'PY'
import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "message-board.settings.dev.local_postgres",
)

import django
django.setup()

from django.conf import settings
from django.db import connection
from demo.models import Message

print("SETTINGS MODULE:", os.environ["DJANGO_SETTINGS_MODULE"])
print("ENGINE:", settings.DATABASES["default"]["ENGINE"])
print("NAME:", settings.DATABASES["default"]["NAME"])
print("HOST:", settings.DATABASES["default"].get("HOST"))
print("DB VENDOR:", connection.vendor)

print("MESSAGES:")
for m in Message.objects.order_by("id"):
    print(m.id, m.text, m.created_at)
PY
SETTINGS MODULE: message-board.settings.dev.local_postgres
ENGINE: django.db.backends.postgresql
NAME: message-board
HOST: database
DB VENDOR: postgresql
MESSAGES:
1 hi 2026-09-22 18:13:01.233327+00:00
2 this is a test 2026-09-22 18:13:15.763124+00:00
3 My name is Roni 2026-09-22 18:14:27.197138+00:00
4 testing 09/23/2026 2026-09-23 13:52:55.228302+00:00
5 csrf test 2026-09-23 14:28:50.528779+00:00
6 zap itig message 2026-09-23 14:30:14.211900+00:00
7 another test 2026-09-23 15:14:56.996150+00:00
8 test after wget mitig 2026-09-23 15:25:43.928780+00:00
9 another test 45 2026-09-23 15:30:01.607296+00:00
10 docker wget remove 2026-09-23 16:04:55.849663+00:00
11 from superuser 2026-09-23 17:21:56.384213+00:00
12 test after frontend wget 2026-09-23 17:52:39.124304+00:00
13 testy 2026-09-23 18:02:45.343622+00:00
14 hello again 2026-09-23 18:09:10.285768+00:00
15 hey 2026-09-23 18:10:44.589393+00:00
ronicbrown@CAZVW0FVAA3-59K:~/message-board/app$
