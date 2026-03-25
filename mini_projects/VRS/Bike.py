from Vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, price, engine, bike_type):
        super().__init__(vehicle_id, brand, model, price)
        self.engine_capacity = engine
        self.bike_type = bike_type

    def display_info(self):
        print("Bike:", self.vehicle_id, self.brand, self.model, self.engine_capacity)

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days