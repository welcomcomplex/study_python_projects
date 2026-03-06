class Calculator:
    def __init__(self, name: str):
        self.name = name
    def add(self, a, b):
        return a + b
    
    @classmethod
    def get_name(cls):
        return cls.name
    @staticmethod
    def is_positive(n):
        return n > 0
    
  