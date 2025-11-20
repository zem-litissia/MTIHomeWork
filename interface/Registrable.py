from abc import ABC, abstractmethod
class Registrable(ABC):
    @abstractmethod
    def register_member(self, member):
        """Register a member in an event or activity"""
        pass