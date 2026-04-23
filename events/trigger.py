import time
import os
from function import process_file

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

print(f"--- Event-Driven Workflow Simulator (Chapter 11) ---")
print(f"Monitoring folder: {UPLOAD_DIR}")
print(f"Waiting for file uploads...")

processed_files = set()

try:
    while True:
        # Check for new files in the 'uploads' directory
        current_files = set(os.listdir(UPLOAD_DIR))
        new_files = current_files - processed_files
        
        for file_name in new_files:
            file_path = os.path.join(UPLOAD_DIR, file_name)
            if os.path.isfile(file_path):
                print(f"\n[Event Trigger] Detected new file: {file_name}")
                process_file(file_path)
                processed_files.add(file_name)
        
        time.sleep(2) # Poll every 2 seconds
except KeyboardInterrupt:
    print("\nSimulator stopped.")
