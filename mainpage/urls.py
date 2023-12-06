from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="post"),
    path("/datatest", views.register_submit, name='datatest')
]