from django.urls import path
from .views import index, health_check, upload_file

urlpatterns = [
    path("", index, name="index"),
    path("api/health/", health_check, name="health_check"),
    path("api/upload/", upload_file, name="upload_file"),
]