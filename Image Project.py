import os
import shutil

def organize_jpg_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        
    files = os.listdir(source_folder)
    
    for file in files:
        if file.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            
            shutil.move(source_path, destination_path)
            print(f"Moved: {file}")

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

source = os.path.join(desktop_path, "Photos")
destination = os.path.join(desktop_path, "Moved_JPGs")

organize_jpg_files(source, destination)