from vehicles.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, distance, load, fuel_price):
        super().__init__(distance, load, fuel_price)

    def calculate_fuel_consumption(self):
        base_consumption = 8
        adjustment_factor = 1 + (self.load / 100) * 0.2
        return (base_consumption * adjustment_factor * self.distance) / 100