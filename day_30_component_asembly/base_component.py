from typing import Optional
from abc import ABC, abstractmethod

class BaseComponent(ABC):
    @abstractmethod
    def run(self, filename: str, folder: str ) -> None:
        pass


