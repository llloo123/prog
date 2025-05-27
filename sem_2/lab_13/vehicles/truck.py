from vehicles.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, distance, load, fuel_price):
        super().__init__(distance, load, fuel_price)

    def calculate_fuel_consumption(self):
        base_consumption = 25  # Базовый расход топлива (л/100км)
        adjustment_factor = 1 + (self.load / 100) * 0.3  # Коэффициент корректировки
        return (base_consumption * adjustment_factor * self.distance) / 100

    def calculate_cost(self):
        return self.calculate_fuel_consumption() * self.fuel_price

    def calculate_time(self):
        average_speed = 60  # Средняя скорость грузового автомобиля (км/ч)
        return self.distance / average_speed

    def __repr__(self):
        return f"Truck({self.distance}, {self.load}, {self.fuel_price})"

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Truck(self.distance * factor, self.load, self.fuel_price)
        raise TypeError("Unsupported operand type for *: 'Truck' and '{}'".format(type(factor).__name__))