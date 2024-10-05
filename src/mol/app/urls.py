from django.urls import path

from . import views

urlpatterns = [
    path("flashcard/<int:id>/", views.flashcard, name="flashcard"),
    path("riigieksam", views.riigieksam, name="riigieksam"),
    path("", views.index, name="index"),
]