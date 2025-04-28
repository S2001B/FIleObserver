from datetime import datetime
import sys
import os

sys.path.append(os.path.curdir)

from day_16_batch_runner.batch_runner import BatchRunner
from day_13_modular_pipeline.renamer import Renamer
from day_13_modular_pipeline.validator import Validator
from day_13_modular_pipeline.file_pipeline import FilePipeline
from day_14_logging_system.logger import Logger
from day_19_log_summary.log_summary import LogSummary
from day_20_rejected_cleanup.cleanup import CleanupTool
from day_21_config_path.config_loader import ConfigLoader
from day_22_zip_files.zip_file import Archiver
from day_23_daily_system_report.daily_report import DailyReporter
from day_25_system_health_checker.system_health import SystemHealth

configurations = ConfigLoader("day_21_config_path\\config.json")
new_logger = Logger(configurations.get("log"))
new_log_summary = LogSummary(new_logger)
new_renamer = Renamer(configurations.get("rules"), logger=new_logger)
new_validator = Validator(configurations.get("self_config"), logger=new_logger)

new_pipe = FilePipeline(new_renamer, new_validator)
downloads = configurations.get("downloads")
runner = BatchRunner(new_pipe, downloads)

new_archiver = Archiver(configurations.get("uploads"), configurations.get("archives"), config=configurations, logger=new_logger)

cleaner = CleanupTool(configurations.get("rejected"), logger=new_logger)
days_old = 2

new_reporter = DailyReporter(configurations.get("log"), configurations.get("output"))
new_health_checker = SystemHealth(configurations.get("self_config"), new_logger)

while True:

    date, time = datetime.now().strftime("%Y-%m-%d %H-%M-%S").split(" ")    

    print("\n--- FILE OBSERVER CONTROL PANEL ---")
    print(f"Date: {date}     Time: {time}".center(30), end="\n\n")
    print("File Watcher: 1\t\t" \
            "Files Parser: 2\n" \
            "Read Log File: 3\t" \
            "Log Summary: 4\n" \
            "Clean Rejected: 5\t" \
            "Archive (ZIP): 6\n" \
            "System Health: 7\t" \
            "Daily Report: 8\n" \
            "Info (Guide): 9\t\t" \
            "Quit: q")

    inp = input("\nYour Choice: ")

    match inp:
        case "1":
            os.system("cls")
            runner.run_loop()
        case "2":
            os.system("cls")
            runner.run_all()
        case "3":
            os.system("cls")
            new_logger.read_grouped()
        case "4":
            os.system("cls")
            print(new_log_summary.log_summary())
        case "5":
            os.system("cls")
            cleaner.run(days_old=days_old)
        case "6":
            os.system("cls")
            new_archiver.run()
        case "7":
            os.system("cls")
            new_health_checker.verify_folders()
        case "8":
            os.system("cls")
            new_reporter.generate_report()
        case "9":
            os.system("cls")
            print("1._File Watcher_ -> Monitors a filder, when a new entry occurs, the file is transfered depending on its name and contents.\n" \
            "2._Files Parser_ -> Parses all files in a folder, untill None are left. If no files exist in the folder the script does not run.\n" \
            "3._Read File Log_ -> Reads the context of the file log (all logged events) and returns the contents.\n" \
            "4._Log Summary_ -> Reads the number of context lines in the log file and returns all events in numbers.\n" \
            f"5._Clean Rejected_ -> Clears the rejected files form the specified folder, files must be older than {days_old} days.\n" \
            "6._Archiver (ZIP)_ -> Copies all files in /uploads and creates a ZIP in /archives.\n" \
            "7._System Health_ -> Reviews all folders and restores the ones deleted or damaged\n" \
            f"8._Daily Report_ -> Returns all activities logged in the past {new_reporter.hours} hours ".upper())
        case "q" | "Q":
            break

        
    


