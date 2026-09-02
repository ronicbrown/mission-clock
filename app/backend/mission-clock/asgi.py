"""
ASGI config for mission-clock project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mission-clock.settings.dev.local_postgres")

application = get_asgi_application()
