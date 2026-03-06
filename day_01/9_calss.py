class Product:
    def __init__(self):
        self.name = "iPhone"
        self.price = 999
        self.quantity = 10
    def total_value(self):
        return self.price * self.quantity

class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand: str, model: str):
            super().__init__(brand)
            self.model = model
        # ← 请在这里补全代码，确保 brand 和 model 都被正确初始化

class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.logs = []

