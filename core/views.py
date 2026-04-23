import sys
import os
import json
from django.conf import settings
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

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        
        # Path to Chapter 11 uploads directory
        upload_dir = os.path.join(settings.BASE_DIR, 'events', 'uploads')
        os.makedirs(upload_dir, exist_ok=True)
        
        file_path = os.path.join(upload_dir, uploaded_file.name)
        
        # Save the file
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        
        return JsonResponse({
            "status": "success",
            "message": f"File '{uploaded_file.name}' uploaded successfully to storage. Event trigger will process it shortly.",
            "file_name": uploaded_file.name
        })
    
    return JsonResponse({"status": "error", "message": "Only POST requests with a file are allowed."}, status=400)

def event_logs(request):
    log_dir = os.path.join(settings.BASE_DIR, 'events', 'logs')
    logs = []
    
    if os.path.exists(log_dir):
        for filename in os.listdir(log_dir):
            if filename.endswith('_metadata.json'):
                with open(os.path.join(log_dir, filename), 'r') as f:
                    logs.append(json.load(f))
    
    # Sort logs by processed_at descending
    logs.sort(key=lambda x: x.get('processed_at', ''), reverse=True)
    
    context = {
        "logs": logs,
        "name": "Group 10"
    }
    return render(request, "event_details.html", context)
