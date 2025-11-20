from abc import ABC, abstractmethod
class StorageInterface(ABC):
    @abstractmethod
    def load(self, filename):
        """Load data from a file"""
        pass
