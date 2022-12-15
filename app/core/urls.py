from django.contrib import admin
from django.urls import include, path

from uploadtest.views import image_upload

from . import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core_views.landing_page, name="core-landing"),
    path("upload", image_upload, name="upload"),
]
