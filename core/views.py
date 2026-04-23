import sys
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse

def index(request):
    name = "Group 10"
    Course ="Cloud Computing"
    level = "Level 4"
    lecturer="Dr.  Irene" 
    GroupMembers=[
        {"name": "NDOLI Jean Damascene", "reg": "222002552"},
        {"name": "UMUTONI Belise", "reg": "222015705"},
        {"name": "MUHIRWA Joyeuse Sainte Trinite", "reg": "222004833"},
        {"name": "TUYIZERE Claude", "reg": "222012926"},
        {"name": "NTAWURENZINGABIRE Dorothee", "reg": "222018712"},
        {"name": "NSHUTI Maurice", "reg": "222005714"},
        {"name": "NGOGA NIYOMANA Pacifique", "reg": "218002567"}
    ]  

    data = {
        "name": name,
        "GroupMembers": GroupMembers,
        "course": Course,
        "level": level,
        "lecturer": lecturer,
        "server_time": timezone.now(),
        "python_version": sys.version.split()[0]
    }
    return render(request, "index.html", data)

def health_check(request):
    return JsonResponse({
        "status": "healthy",
        "timestamp": timezone.now().isoformat(),
        "python_version": sys.version,
        "platform": sys.platform
    })