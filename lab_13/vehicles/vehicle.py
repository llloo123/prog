from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, distance, load, fuel_price):
        self._distance = distance
        self._load = load
        self._fuel_price = fuel_price

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        if value < 0:
            raise ValueError("Distance cannot be negative.")
        self._distance = value

    @property
    def load(self):
        return self._load

    @load.setter
    def load(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Load must be between 0 and 100.")
        self._load = value

    @property
    def fuel_price(self):
        return self._fuel_price

    @fuel_price.setter
    def fuel_price(self, value):
        if value < 0:
            raise ValueError("Fuel price cannot be negative.")
        self._fuel_price = value

    @abstractmethod
    def calculate_fuel_consumption(self):
        """Расчет расхода топлива."""
        pass

    @abstractmethod
    def calculate_cost(self):
        """Расчет стоимости поездки."""
        pass

    @abstractmethod
    def calculate_time(self):
        """Расчет времени поездки."""
        pass

    def __str__(self):
        return f"Vehicle(distance={self.distance}, load={self.load}%, fuel_price=${self.fuel_price})"