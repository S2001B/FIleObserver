import shutil
import os
import json
import time
import day_10_secure_file_validation.defensive as defender
from datetime import datetime
from pathlib import Path
from day_30_component_asembly.day_30_deep_scanner.deep_scanner import DeepScanner

def process_file(filename):
    try:
        scanner = DeepScanner()

        curent_directory = os.path.dirname(os.path.realpath(__file__))
        json_file = os.path.join(curent_directory, "config.json") 

        with open(json_file, "r") as f:
            config = json.load(f)

        purgatory = Path(config["purgatory"])
        rejected = Path(config["rejected"])
        downloads = Path(config["downloads"])
        uploads = Path(config["uploads"])
        temp = Path(config["temp"])

        timestamp = datetime.now().strftime("%y-%m-%d-%H-%M-%S")

        with open (os.path.join(curent_directory, "log.txt"), "a") as writer:
            clean = defender.get_clean_filename(filename)
            file_full_path = os.path.join(downloads, filename)

            if clean != filename:
                purgatory_file_location = os.path.join(purgatory, clean)
                shutil.move(file_full_path, purgatory_file_location)
                writer.write(f"{timestamp}: Suspicious file renamed from |{filename}| to |{clean}| -> moved to |{purgatory}|\n")
            
                if scanner.run(filename=purgatory_file_location, folder=rejected):
                    return filename

                rejected_file_location = os.path.join(rejected, clean)
                shutil.move(purgatory_file_location, rejected_file_location)
                writer.write(f"{timestamp}: Tests failed, suspicious file |{clean}| moved to -> |{rejected}|\n")
            

            else:
                temp_file_location =  os.path.join(temp, filename)
                shutil.move(file_full_path, temp_file_location)
                writer.write(f"{timestamp}: File |{filename}| successfully parsed to -> |{temp}| awaiting confirmation\n")

                if scanner.run(filename=temp_file_location, folder=rejected):
                    return filename

                uploads_file_location = os.path.join(uploads, filename)
                shutil.move(temp_file_location, uploads_file_location)
                writer.write(f"{timestamp}: File |{filename}| successfully uploaded to -> |{uploads}|\n")

            return clean

    except (FileNotFoundError, UnicodeError):
        return None

if __name__ == "__main__":
    print("Running file!")
