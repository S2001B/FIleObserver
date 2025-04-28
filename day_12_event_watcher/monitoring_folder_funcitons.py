import time
from  datetime import datetime
from os import path, listdir

downloads_folder_path = path.join(path.abspath("Day10_SecureFileValidation"), "downloads")
length_begining = listdir(downloads_folder_path)

def watch_folder(file):

    state = True
    print(f"Watching folder: {downloads_folder_path}")

    files_found = set(length_begining)

    while state:
        
        length_dynamic = listdir(file)
        print(f"Found files: {listdir(file)}")

        for file_name in length_dynamic:
            if file_name not in files_found:

                time_of_event = datetime.now().strftime("%H-%M-%S")

                print(f"New file detected: |{file_name}| at {time_of_event}")

                files_found = set(length_dynamic)

        time.sleep(3)


watch_folder(downloads_folder_path)