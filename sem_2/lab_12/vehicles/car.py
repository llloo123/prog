class Car:
    def __init__(self, distance, load, fuel_price):
        self.distance = distance  # Расстояние в километрах
        self.load = load          # Загрузка в процентах (0-100)
        self.fuel_price = fuel_price  # Цена топлива за литр

    def calculate_fuel_consumption(self):
        base_consumption = 8  # Базовый расход топлива (л/100км)
        adjustment_factor = 1 + (self.load / 100) * 0.2  # Коэффициент корректировки
        return (base_consumption * adjustment_factor * self.distance) / 100

    def calculate_cost(self):
        fuel_consumption = self.calculate_fuel_consumption()
        return fuel_consumption * self.fuel_price

    def calculate_time(self):
        average_speed = 90  # Средняя скорость легкового автомобиля (км/ч)
        return self.distance / average_speed


