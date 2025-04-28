from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import sys

sys.path.append(os.curdir)


import day_10_secure_file_validation.file_funcitons as day_10
import day_11_smart_renamer.file_name_manipulation as day_11


def file_event(event):
    if not event.is_directory:
        filename = os.path.basename(event.src_path)
        print(f"Folder contents: {os.listdir(downloads_folder)}")
        
    return filename

def separator_ux():
    print("-" * 25, end="\n")


class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        filename = file_event(event=event)
        print(f"New file detected: {filename}")
        separator_ux()

        new_name = day_11.rename_file(filename, downloads_folder)
        day_10.process_file(new_name)
        
        
    def on_moved(self, event):
        filename = file_event(event=event)    
        print(f"File {filename} was renamed")
        separator_ux()

    def on_deleted(self, event):
        filename = file_event(event=event)
        print(f"File {filename} was removed/deleted")
        separator_ux()



def watch_folder(folder_path):
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()

    print(f"Watching (in real-time): {folder_path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

parent = os.path.abspath(os.curdir)
# print(parent)
downloads_folder = os.path.join(parent, "day_10_secure_file_validation\\downloads")
# print(downloads_folder)

# 👇 Change this to your real folder

if not os.path.exists(downloads_folder):
    os.makedirs(downloads_folder)

watch_folder(downloads_folder)
