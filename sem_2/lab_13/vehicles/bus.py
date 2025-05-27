from vehicles.vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, distance, load, fuel_price):
        super().__init__(distance, load, fuel_price)

    def calculate_fuel_consumption(self):
        base_consumption = 20  # Базовый расход топлива (л/100км)
        adjustment_factor = 1 + (self.load / 100) * 0.25  # Коэффициент корректировки
        return (base_consumption * adjustment_factor * self.distance) / 100

    def calculate_cost(self):
        return self.calculate_fuel_consumption() * self.fuel_price

    def calculate_time(self):
        average_speed = 70  # Средняя скорость автобуса (км/ч)
        return self.distance / average_speed

    def __repr__(self):
        return f"Bus({self.distance}, {self.load}, {self.fuel_price})"

    def __sub__(self, other):
        if isinstance(other, Bus):
            return Bus(self.distance - other.distance, self.load, self.fuel_price)
        raise TypeError("Unsupported operand type for -: 'Bus' and '{}'".format(type(other).__name__))