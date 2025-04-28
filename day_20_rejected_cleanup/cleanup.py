from datetime import datetime, timedelta
import os
import sys

sys.path.append(os.path.curdir)

from day_26_file_handler_base.file_handler_base import FileHandlerBase

class CleanupTool(FileHandlerBase):
    def __init__(self, folder: str, logger=None):
        self.folder = folder
        self.logger = logger

    def clean(self, days_old: int = 3):
        cutoff = datetime.now() - timedelta(days=days_old)
        files = os.listdir(self.folder)

        for file in files:
            file_path = os.path.join(self.folder, file)

            if not os.path.isfile(file_path):
                continue  # skip folders

            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))

            if file_modified_time < cutoff:
                os.remove(file_path)
                if self.logger:
                    self.logger.info(f"Deleted old file: {file} (Last modified: {file_modified_time.strftime('%Y-%m-%d %H:%M:%S')})")

    def run(self, days_old):
        return self.clean(days_old)

