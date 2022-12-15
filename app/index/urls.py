from django.contrib import admin
from django.urls import path

from . import views as app_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("/", app_views.landing_page, name="app-landing"),
]
