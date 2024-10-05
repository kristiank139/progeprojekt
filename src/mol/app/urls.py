from django.urls import path

from . import views

urlpatterns = [
    path("flashcards/<str:aine>/", views.flashcards, name="flashcards"),
    path("riigieksam", views.riigieksam, name="riigieksam"),
    path("", views.index, name="index"),
]