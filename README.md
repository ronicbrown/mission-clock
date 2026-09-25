ronicbrown@CAZVW0FVAA3-59K:~/message-board/app/.gitlab/expedition-0/prod$ cd ~/message-board/app

grep -RIn \
  "DB_HOST\|DB_NAME\|DB_USER\|DB_PASS\|DB_PORT\|SECRET_KEY" \
  backend/message-board/settings
backend/message-board/settings/dev/.env.backup:1:DB_NAME="message-board"
backend/message-board/settings/dev/.env.backup:2:DB_USER="postgres"
backend/message-board/settings/dev/.env.backup:3:DB_PASS="UVNLdTIFzxYle0U5"
backend/message-board/settings/dev/.env.backup:4:DB_HOST="database"
backend/message-board/settings/dev/.env.backup:5:DB_PORT="5432"
backend/message-board/settings/dev/.env.backup:6:DB_NAME="message-board"
backend/message-board/settings/dev/.env.backup:7:DB_USER="postgres"
backend/message-board/settings/dev/.env.backup:8:DB_PASS="OjWwmOmSm7CaVdyZ"
backend/message-board/settings/dev/.env.backup:9:DB_HOST="database"
backend/message-board/settings/dev/.env.backup:10:DB_PORT="5432"
backend/message-board/settings/dev/.env.backup:11:DB_NAME="message-board"
backend/message-board/settings/dev/.env.backup:12:DB_USER="postgres"
backend/message-board/settings/dev/.env.backup:13:DB_PASS="RZQczfKg3luYqSnb"
backend/message-board/settings/dev/.env.backup:14:DB_HOST="database"
backend/message-board/settings/dev/.env.backup:15:DB_PORT="5432"
backend/message-board/settings/dev/.env.backup:16:DB_NAME="message-board"
backend/message-board/settings/dev/.env.backup:17:DB_USER="postgres"
backend/message-board/settings/dev/.env.backup:18:DB_PASS="Hf8sN3byk10Sx4B6"
backend/message-board/settings/dev/.env.backup:19:DB_HOST="database"
backend/message-board/settings/dev/.env.backup:20:DB_PORT="5432"
backend/message-board/settings/dev/.env.backup:21:DB_NAME="message-board"
backend/message-board/settings/dev/.env.backup:22:DB_USER="postgres"
backend/message-board/settings/dev/.env.backup:23:DB_PASS="TSwC4NGQEIcEvCA1"
backend/message-board/settings/dev/.env.backup:24:DB_HOST="database"
backend/message-board/settings/dev/.env.backup:25:DB_PORT="5432"
backend/message-board/settings/dev/local_postgres.py:18:SECRET_KEY = "django-insecure-u8^#*!f@4%gpodaniz_7*x8vv^92d!5nccb_1-m!msjr9#lp*6"
backend/message-board/settings/dev/local_postgres.py:26:        "NAME": os.environ["DB_NAME"],
backend/message-board/settings/dev/local_postgres.py:27:        "USER": os.environ["DB_USER"],
backend/message-board/settings/dev/local_postgres.py:28:        "PASSWORD": os.environ["DB_PASS"],
backend/message-board/settings/dev/local_postgres.py:29:        "HOST": os.environ["DB_HOST"],
backend/message-board/settings/dev/local_postgres.py:30:        "PORT": os.environ["DB_PORT"],
backend/message-board/settings/dev/postgres_flexible_server.py:13:# Ensure you add a SECRET_KEY value to the environment of the deployed container!
backend/message-board/settings/dev/postgres_flexible_server.py:14:SECRET_KEY = os.environ["SECRET_KEY"]
backend/message-board/settings/dev/postgres_flexible_server.py:22:        "NAME": os.environ["DB_NAME"],
backend/message-board/settings/dev/postgres_flexible_server.py:23:        "USER": os.environ["DB_USER"],
backend/message-board/settings/dev/postgres_flexible_server.py:24:        "PASSWORD": os.environ["DB_PASS"],
backend/message-board/settings/dev/postgres_flexible_server.py:25:        "HOST": os.environ["DB_HOST"],
backend/message-board/settings/dev/postgres_flexible_server.py:26:        "PORT": os.environ["DB_PORT"],
backend/message-board/settings/dev/.env:1:DB_NAME="message-board"
backend/message-board/settings/dev/.env:2:DB_USER="postgres"
backend/message-board/settings/dev/.env:3:DB_PASS="aojHf8TKXcZVmo3O"
backend/message-board/settings/dev/.env:4:DB_HOST="database"
backend/message-board/settings/dev/.env:5:DB_PORT="5432"
backend/message-board/settings/dev/local.py:12:SECRET_KEY = "django-insecure-u8^#*!f@4%gpodaniz_7*x8vv^92d!5nccb_1-m!msjr9#lp*6"
backend/message-board/settings/test/postgres_flexible_server.py:13:# Ensure you add a SECRET_KEY value to the environment of the deployed container!
backend/message-board/settings/test/postgres_flexible_server.py:14:SECRET_KEY = os.environ["SECRET_KEY"]
backend/message-board/settings/test/postgres_flexible_server.py:22:        "NAME": os.environ["DB_NAME"],
backend/message-board/settings/test/postgres_flexible_server.py:23:        "USER": os.environ["DB_USER"],
backend/message-board/settings/test/postgres_flexible_server.py:24:        "PASSWORD": os.environ["DB_PASS"],
backend/message-board/settings/test/postgres_flexible_server.py:25:        "HOST": os.environ["DB_HOST"],
backend/message-board/settings/test/postgres_flexible_server.py:26:        "PORT": os.environ["DB_PORT"],
backend/message-board/settings/prod/postgres_flexible_server.py:20:# Ensure you add a SECRET_KEY value to the environment of the deployed container!
backend/message-board/settings/prod/postgres_flexible_server.py:21:SECRET_KEY = os.environ["SECRET_KEY"]
backend/message-board/settings/prod/postgres_flexible_server.py:29:        "NAME": os.environ["DB_NAME"],
backend/message-board/settings/prod/postgres_flexible_server.py:30:        "USER": os.environ["DB_USER"],
backend/message-board/settings/prod/postgres_flexible_server.py:31:        "PASSWORD": os.environ["DB_PASS"],
backend/message-board/settings/prod/postgres_flexible_server.py:32:        "HOST": os.environ["DB_HOST"],
backend/message-board/settings/prod/postgres_flexible_server.py:33:        "PORT": os.environ["DB_PORT"],
ronicbrown@CAZVW0FVAA3-59K:~/message-board/app$
