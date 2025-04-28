from datetime import datetime
import zipfile
import os
import sys

sys.path.append(os.path.curdir)

from day_26_file_handler_base.file_handler_base import FileHandlerBase

class Archiver(FileHandlerBase):
    def __init__(self, target_folder: str, archive_folder: str, config=None, logger=None):
        self.target = target_folder
        self.archive = archive_folder
        self.logger = logger
        self.config = config

    def zip_validated_files(self):
        base_folder = os.path.basename(self.target)
        listed = os.listdir(self.target)
        self.file_count = 0
        date = datetime.now().strftime("%y-%m-%d-%H-%M-%S")

        if not listed:
            if self.logger:
                self.logger.info(f"No files found in {base_folder} to archive.")
            return

        zip_name = f"archive_{date}.zip"
        zip_path = os.path.join(self.archive, zip_name)

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive_zip:
            for file in listed:
                file_path = os.path.join(self.target, file)
                if os.path.isfile(file_path):
                    archive_zip.write(file_path, arcname=file)
                    self.file_count += 1

        if self.logger:
            self.logger.info(f"Archived {self.file_count} files from {base_folder} into {zip_name}")

    def run(self):
        return self.zip_validated_files()


# from day_21_config_path.config_loader import ConfigLoader
# from day_14_logging_system.logger import Logger

# new_config = ConfigLoader("day_21_config_path\\config.json")
# log = Logger(new_config.get("log"))

# archiver = Archiver(new_config.get("uploads"), new_config.get("archives"), logger=log)
# archiver.zip_validated_files()