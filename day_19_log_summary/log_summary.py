import sys
import os

sys.path.append(os.path.curdir)

from day_14_logging_system.logger import Logger
from day_26_file_handler_base.file_handler_base import FileHandlerBase

class LogSummary(FileHandlerBase):
    def __init__(self, logger: Logger):
        self.logger = logger

    def log_summary(self):
        with open(self.logger.log_path, "r") as reader:
            lines = reader.readlines()
            
            self.entries: int = 0
            self.renamed: int = 0
            self.uploads: int = 0
            self.rejected: int = 0
            self.warnings: int = 0
            self.errors: int = 0

            for line in lines:
                self.entries += 1
            
                if line.__contains__("rejected"):
                    self.rejected += 1

                elif line.__contains__("renamed"):
                    self.renamed += 1

                elif line.__contains__("uploads") or line.__contains__("uploaded"):
                    self.uploads += 1

                elif line.__contains__("ERROR"):
                    self.errors += 1

                elif line.__contains__("WARNING"):
                    self.warnings += 1

            last = lines[-1] if lines else "No recent events found."

            report = "\n".join([
            "\n--- FILE OBSERVER SUMMARY ---",
                f"Total entries: {self.entries}",
                f"Renamed files: {self.renamed}",
                f"Rejected files: {self.rejected}",
                f"Uploaded files: {self.uploads}",
                f"Warnings: {self.warnings}",
                f"Errors: {self.errors}",
                f"Last action:: {last}"])

            # print(report)
            return report
        
    def run(self):
        self.log_summary()

# log = LogSummary(Logger("day_10_secure_file_validation\\log.txt"))
# log.log_summary()


        