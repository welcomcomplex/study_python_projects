class Temperature:
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit
    @property
    def celsius(self):        return self._celsius
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
    @property
    def fahrenheit(self):        return self._fahrenheit
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._fahrenheit = value
        self._celsius = (value - 32) * 5 / 9


class User:
    def __init__(self, name):
        self._name = name  # ← 这里调用 setter！

    @property
    def name(self):
        return self._name  # ← 这里也调用 getter！→ 无限递归

    @name.setter
    def name(self, value):
        self._name = value  # ← 错误：又调用 setter！

class NonemptyString:
    def __init__(self,name):
        self.name = name
    def __get__(self,obj,objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    def __set__(self,obj,value):
        if not isinstance(value,str) or not value:
            raise ValueError('Must be a nonempty string')
        obj.__dict__[self.name] = value
