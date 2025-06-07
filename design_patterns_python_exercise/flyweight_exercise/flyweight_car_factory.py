from abc import ABC, abstractmethod


class CarPart(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Engine(CarPart):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Car:
    def __init__(self, VIN, color, engine):
        self.engine = engine
        self.VIN = VIN
        self.color = color

    def __str__(self):
        return f"This {self.color} car have {self.engine} engine"


class CarFactory:
    _engines = {}

    def get_engine(self, engine):
        if engine not in self._engines:
            self._engines[engine] = Engine(engine)
        return self._engines[engine]


factory = CarFactory()
car1 = Car("1HGCM82633A004352", "Red", factory.get_engine("V8"))
car2 = Car("1HGCM82633A004353", "Blue", factory.get_engine("V8"))
car3 = Car("1HGCM82633A004354", "Black", factory.get_engine("V6"))

print(car1)
print(car2)
print(car3)

print(car1.engine is car2.engine)  # True
print(car1.engine is car3.engine)  # False
