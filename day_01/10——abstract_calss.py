from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"

class AIService(ABC):
    def __init__(self, name: str):
        self.name = name 
    @abstractmethod
    def infer(self, input_data: dict) -> dict:
        pass
    @abstractmethod
    def health_check(self) -> bool:
        pass
                