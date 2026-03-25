from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, price, doors, fuel):
        super().__init__(vehicle_id, brand, model, price)
        self.num_doors = doors
        self.fuel_type = fuel

    def display_info(self):
        print("Car:", self.vehicle_id, self.brand, self.model, self.num_doors, self.fuel_type)

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days