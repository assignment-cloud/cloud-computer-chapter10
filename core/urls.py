from django.urls import path
from .views import index, health_check, upload_file, event_logs

urlpatterns = [
    path("", index, name="index"),
    path("api/health/", health_check, name="health_check"),
    path("api/upload/", upload_file, name="upload_file"),
    path("events/", event_logs, name="event_logs"),
]