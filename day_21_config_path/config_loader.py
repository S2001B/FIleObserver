import os
import sys
import json

sys.path.append(os.path.curdir)

class ConfigLoader:
    def __init__(self, path: str):
        with open(path, "r") as reader:
            self.path = json.load(reader)

    def get(self, key: str) -> str:
        for conf_key, conf_val in self.path.items():

            if key.lower() == conf_key.lower():
                # print(self.path[key])
                return conf_val
            
        raise KeyError(f"Key '{key}' not found in config.")

    def show(self):
        for key, value in self.path.items():
            print(f"{key}: {value}")
