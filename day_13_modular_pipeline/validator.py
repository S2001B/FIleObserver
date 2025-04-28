import sys
import os
import json

sys.path.append(os.path.curdir)

import day_10_secure_file_validation.file_funcitons as process
from day_26_file_handler_base.file_handler_base import FileHandlerBase

class Validator(FileHandlerBase):
    def __init__(self, config_path: str, logger=None):
        self.logger = logger
        with open(config_path) as conf:
            self.conf = json.load(conf)


    def validate(self, filename: str):
        if filename:
            clean = process.process_file(filename)

        else:
            return

        if clean != filename:
            self.logger.warning(f"Suspicious filename detected: {filename}")
            self.logger.info(f"File moved to purgatory: {clean}")
            self.logger.error(f"File rejected after failed checks: {clean}")
        
        else:
            self.logger.info(f"File validated and moved to temp: {filename}")
            self.logger.info(f"File uploaded: {filename}") 

    def run(self, filename: str):
        return self.validate(filename)
    
