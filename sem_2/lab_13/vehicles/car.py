from vehicles.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, distance, load, fuel_price):
        super().__init__(distance, load, fuel_price)

    def calculate_fuel_consumption(self):
        base_consumption = 8
        adjustment_factor = 1 + (self.load / 100) * 0.2
        return (base_consumption * adjustment_factor * self.distance) / 100
    
    def calculate_cost(self):
        return self.calculate_fuel_consumption() * self.fuel_price

    def calculate_time(self):
        average_speed = 60  
        return self.distance / average_speed

    def __repr__(self):
        return f"Car({self.distance}, {self.load}, {self.fuel_price})"

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Car(self.distance * factor, self.load, self.fuel_price)
        raise TypeError("Unsupported operand type for *: 'Car' and '{}'".format(type(factor).__name__))
