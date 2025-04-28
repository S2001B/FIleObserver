import os
import json
import sys

sys.path.append(os.path.curdir)
print(os.path.curdir)

import day_11_smart_renamer.file_name_manipulation as rename_validator
from day_26_file_handler_base.file_handler_base import FileHandlerBase

class Renamer(FileHandlerBase):
    def __init__(self, rules_path: str, logger=None):
        self.logger = logger
        with open(rules_path) as rules:
            self.rules = json.load(rules)

    def rename(self, filename: str, folder: str) -> str:
        new_name = rename_validator.rename_file(filename, folder)
        if new_name != filename:
            self.logger.info(f"Renamed file: {filename} → {new_name}")
        # print(f"[] {filename} → {new_name}")
        return new_name

    def run(self, filename: str, folder: str):
        return self.rename(filename, folder)


