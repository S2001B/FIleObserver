import os
import sys
import shutil
from typing import Union

sys.path.append(os.path.curdir)

from day_26_file_handler_base.file_handler_base import FileHandlerBase
from day_21_config_path.config_loader import ConfigLoader
from day_14_logging_system.logger import Logger

class DeepScanner(FileHandlerBase):
    def __init__(self):
        self.DANGEROUS_EXTENSIONS = [
        ".exe", ".bat", ".sh", ".vbs",
        ".js", ".scr", ".cmd", ".ps1", 
        ".dll", ".php"
        ]

        self.MAGIC_NUMBERS = {
        "exe": b"MZ",
        "pdf": b"%PDF",
        "zip": b"PK",
        "jpg": b"\xFF\xD8\xFF",
        "png": b"\x89PNG",
        }

        self.DANGEROUS_KEYWORDS = [
        "powershell",
        "Invoke-WebRequest",
        "cmd.exe",
        "wget",
        "curl",
        "Start-Process",
        "rm -rf",
        "<script>",
        ]

        self.UNICODE_TRAPS = ["\u200b", "\u200d", "\ufeff"]

        config = ConfigLoader("day_21_config_path\\config.json")
        self.logger = Logger(config.get("log"))
        

    def run(self, filename: str, folder: Union[str, None]) -> Union[bool, None]:
        try:
            name, ext = os.path.splitext(os.path.basename(filename))
            ext = ext.lower()

            # Check magic number
            magic_matched = False
            with open(filename, "rb") as file:
                file_start = file.read(8)

            for file_type, signature in self.MAGIC_NUMBERS.items():

                if file_start.startswith(signature):
                    magic_matched = True

                    if ext.replace(".", "") == file_type:
                        self.logger.info(f"File type matched: {file_type} = {ext}")
                    else:
                        self.logger.warning(f"File type mismatch: {file_type} vs {ext}")
                    break

            if not magic_matched:
                self.logger.warning(f"Unknown magic number in {filename}")

            # Check for dangerous keywords (only for scripts)
            dangerous_keyword_found = False
            suspicious = False
            ext_expression = (ext in self.DANGEROUS_EXTENSIONS) or ext.replace(".", "") in self.MAGIC_NUMBERS.keys()

            if ext_expression:     
               
                with open(filename, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read().lower()

                    for keyword in self.DANGEROUS_KEYWORDS:
                        if keyword.lower() in content:
                            self.logger.error(f"Keyword detected in {filename}: {keyword}")

                            dangerous_keyword_found = True
                            break  # no need to scan more if one found

                    for trap in self.UNICODE_TRAPS:
                        if trap in content:
                            self.logger.error(f"Unicode obfuscation detected in {filename}: {repr(trap)}")
                            
                            suspicious = True
                            break

            # Move dangerous file if needed
            if (ext_expression and folder) and (dangerous_keyword_found or suspicious or not magic_matched):
                
                shutil.move(filename, folder)

                message = f"Dangerous file {filename} detected and moved to {folder}"
                self.logger.error(message)
                print(message)

                return suspicious or dangerous_keyword_found
            
            else:
                self.logger.info(f"Scan completed: {filename} safe.")
                
                return None

        except FileNotFoundError:
            self.logger.error(f"File not found: {filename}")
            return None