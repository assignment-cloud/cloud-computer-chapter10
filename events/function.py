import os
import json
from datetime import datetime

def process_file(file_path):
    """
    Simulated Cloud Function: Processes an uploaded file and saves metadata.
    """
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    
    # Metadata to be saved
    metadata = {
        "event": "FILE_UPLOAD",
        "file_name": file_name,
        "size_bytes": file_size,
        "processed_at": datetime.now().isoformat(),
        "status": "SUCCESS"
    }
    
    # Save log/metadata record
    log_dir = os.path.join(os.path.dirname(__file__), "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f"{file_name}_metadata.json")
    with open(log_file, "w") as f:
        json.dump(metadata, f, indent=4)
        
    print(f" [Cloud Function] Processed {file_name}. Metadata saved to logs.")
    return metadata
