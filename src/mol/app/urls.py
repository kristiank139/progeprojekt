from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("flashcards/<str:aine>/", views.flashcards, name="flashcards"),
    path("riigieksam", views.riigieksam, name="riigieksam"),
    path("", views.index, name="index"),

    path("chatRobot", views.chatRobot, name="chatRobot"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)