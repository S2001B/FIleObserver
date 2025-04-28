import sys
import os
import inspect
from typing import Callable

# HandlerValues = list(Callable([str, str], None)) # will be the new type, now no matter what values you put in it is either both or not, whatever runs

sys.path.append(os.path.curdir)

from day_13_modular_pipeline.renamer import Renamer
from day_13_modular_pipeline.validator import Validator
# from day_14_logging_system.logger import Logger

class FilePipeline():
    def __init__(self, renamer:Renamer, validator:Validator):
        self.renamer = renamer
        self.validator = validator

    def run(self, filename: str, folder: str, handlers: list = None):
        # Simulate "overloading" using the presence of `handlers`
        if handlers:
            for handler in handlers:
                args = inspect.signature(handler.run).parameters
                
                if len(args) == 2:
                    handler.run(filename, folder)
                else:
                    handler.run(filename)
        else:
            renamed = self.renamer.run(filename, folder)
            self.validator.run(renamed)



# new_logger = Logger("day_10_secure_file_validation\\log.txt")

# new_renamer = Renamer("day_11_smart_renamer\\rename_rules.json")
# new_validator = Validator("day_10_secure_file_validation\\config.json")

# new_pipe = FilePipeline(new_renamer, new_validator)
# new_pipe.run("C:\\Users\\ststo\\OneDrive\\Desktop\\FileObserver\\$%$£$fsfwrgerg.txt", "C:\\Users\\ststo\\OneDrive\\Desktop\\FileObserver\\day_10_secure_file_validation\\downloads")

        