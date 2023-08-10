import os
import shutil
import time

folder_path = "C:\\POSPac"
cutoff_time = time.time() - 7 * 24 * 60 * 60  # One week ago

for foldername in os.listdir(folder_path):
    subfolder_path = os.path.join(folder_path, foldername)
    if os.path.isdir(subfolder_path):
        if os.path.getmtime(subfolder_path) < cutoff_time:
            shutil.rmtree(subfolder_path)
            print(f"Deleted {subfolder_path}")