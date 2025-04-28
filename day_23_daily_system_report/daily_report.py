import os
import sys
from datetime import datetime, timedelta

sys.path.append(os.path.curdir)

class DailyReporter:
    def __init__(self, log_path: str, output_folder: str):
        self.log_path = log_path
        self.output_folder = output_folder
        self.hours = 24

    def is_recent(self, log_line):  
        try:
            # Split and parse the timestamp from the log format
            parts = log_line.split(" ")
            timestamp_str = parts[1] + " " + parts[2]
            # print(timestamp_str)
            log_time = datetime.strptime(timestamp_str, "%y-%m-%d %H:%M:%S")
            # print(log_time)
            
            return datetime.now() - log_time <= timedelta(hours=self.hours)     
        except:
            return False

    def generate_report(self):
        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)

        # Read and filter log lines directly
        with open(self.log_path, "r") as reader:
            lines = reader.readlines()
            recent_lines = [line for line in lines if self.is_recent(line)]

        # Count event types
        entries = len(recent_lines)
        renamed = sum("renamed" in line.lower() for line in recent_lines)
        rejected = sum("rejected" in line.lower() for line in recent_lines)
        uploaded = sum("upload" in line.lower() for line in recent_lines)
        warnings = sum("warning" in line.lower() for line in recent_lines)
        errors = sum("error" in line.lower() for line in recent_lines)
        last_action = recent_lines[-1] if recent_lines else "No recent events found."

        # Format summary
        summary = f"""\
--- FILE OBSERVER SUMMARY ---
Total entries: {entries}
Renamed files: {renamed}
Rejected files: {rejected}
Uploaded files: {uploaded}
Warnings: {warnings}
Errors: {errors}
Last action: {last_action}"""

        # Save report file
        report_filename = f"report_{datetime.now().strftime('%y-%m-%d')}.txt"
        report_path = os.path.join(self.output_folder, report_filename)

        with open(report_path, "w") as report:
            report.write(summary)

        print(f"[✅] Report saved to: {report_path}")


