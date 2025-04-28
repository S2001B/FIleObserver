import sys
import os
import time

sys.path.append(os.path.curdir)

from day_13_modular_pipeline.file_pipeline import FilePipeline

class BatchRunner():
    def __init__(self, pipeline:FilePipeline, source_path: str):
        self.pipeline = pipeline
        self.source_path = source_path

    def run_all(self):
        if self.pipeline.renamer.logger:
            self.pipeline.renamer.logger.info("[BatchRunner] Starting batch run")
            print("[BatchRunner] Starting batch run")

        for file in os.listdir(self.source_path):
            if_file = os.path.join(self.source_path, file)
            
            if os.path.isfile(if_file):
                self.pipeline.run(file, self.source_path)

        if self.pipeline.renamer.logger:
            self.pipeline.renamer.logger.info("[BatchRunner] Batch run completed")
            print("[BatchRunner] Batch run completed")

    def run_loop(self, delay=5):
        seen = set()

        if self.pipeline.renamer.logger:
            self.pipeline.renamer.logger.info("[BatchRunner] Starting batch run")
            print("[BatchRunner] Starting batch run")

            while True:
                try:
                    current_files = set(os.listdir(self.source_path))
                    new_files = current_files - seen

                    for file in new_files:
                        full_path = os.path.join(self.source_path, file)
                        if os.path.isfile(full_path):
                            self.pipeline.run(file, self.source_path)

                    seen = current_files
                    time.sleep(delay)

                except KeyboardInterrupt:
                    print("[LiveRunner] Stopped by user.")
                    if self.pipeline.renamer.logger:
                        self.pipeline.renamer.logger.info("[LiveRunner] Folder watcher stopped")
                        print("[LiveRunner] Folder watcher stopped")
                    break



    
