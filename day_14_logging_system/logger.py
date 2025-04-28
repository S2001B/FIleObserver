import os
import sys
from datetime import datetime

sys.path.append(os.path.curdir)

class Logger:
    def __init__(self, log_path: str):
        self.log_path = log_path

    def log_body(self, message):
        stamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        return f"{stamp} - {message}"

    def open_file_entry(self, message):
        with open(self.log_path, "a") as info:
            info.write(message + "\n")

    def info(self, message: str):
        writabble = f"[INFO] {self.log_body(message)}"
        self.open_file_entry(writabble)
        # Write a line with "[INFO] <timestamp> message"

    def warning(self, message: str):
        writabble = f"[WARNING] {self.log_body(message)}"
        self.open_file_entry(writabble)
        # Same, but with [WARNING]

    def error(self, message: str):
        writabble = f"[ERROR] {self.log_body(message)}"
        self.open_file_entry(writabble)
        # Same, but with [ERROR]
    
    def allert(self, message: str):
        writabble = f"[ALERT] {self.log_body(message)}"
        self.open_file_entry(writabble) 

    def read(self):
        with open(self.log_path, "r") as reader:
            read = reader.readlines()
            return read
        
    def read_grouped(self):
        with open(self.log_path, "r") as reader:
            read = reader.readlines()
            for line in read:
                print(line.strip())
