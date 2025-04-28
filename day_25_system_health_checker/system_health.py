import os
import sys
import json

sys.path.append(os.path.curdir)

class SystemHealth:
    def __init__(self, config_path: str, logger=None):
        self.config_path = config_path
        self.logger = logger

    def verify_folders(self):
        with open(self.config_path, "r") as config:
            contents = json.load(config)

            for key, path in contents.items():
                if not os.path.exists(path):
                    try:
                        os.makedirs(path)
                        print(f"[WARNING] Missing folder: {path} → Created it")
                        if self.logger:
                            self.logger.warning(f"Missing folder: {path} → Created it")
                    except Exception as e:
                        print(f"[ERROR] Failed to create: {path} ({e})")
                        if self.logger:
                            self.logger.error(f"Failed to create: {path} ({e})")
                else:
                    print(f"[INFO] Checked folder: {path} → OK")
                    if self.logger:
                        self.logger.info(f"Checked folder: {path} → OK")
