from django.contrib import admin
from django.urls import include, path
from mainpage import views

urlpatterns = [
    path("", include("mainpage.urls")),
    path("admin/", admin.site.urls),
]