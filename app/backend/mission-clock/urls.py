"""
URL configuration for mission-clock project.
"""

from django.contrib import admin
from django.urls import path

from demo.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
]
