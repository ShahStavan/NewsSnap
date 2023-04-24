from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("technology/", views.technology, name="technology"),
    path("sports/", views.sports, name="sports"),
    path("entertainment/", views.entertainment, name="entertainment"),
    path("business/", views.business, name="business"),
    path("health/", views.health, name="health"),
    path("science/", views.science, name="science"),
    path("summary/", views.summarizer, name="summarizer"),
]
