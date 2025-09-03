from django.urls import path
from .views import random_name

urlpatterns = [
    path("random-name/", random_name, name="random_name"),
]