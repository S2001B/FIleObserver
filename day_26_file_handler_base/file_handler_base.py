from abc import ABC, abstractmethod

class FileHandlerBase(ABC):
    @abstractmethod
    def run(self, filename: str, folder = None):
        raise NotImplementedError("Subclasses must implement this.")
