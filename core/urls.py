from django.urls import path
from .views import index, health_check

urlpatterns = [
    path("", index, name="index"),
    path("api/health/", health_check, name="health_check"),
]