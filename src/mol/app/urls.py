from django.urls import path

from . import views

urlpatterns = [
    path("<str:aine>", views.index, name="index"),
]