class Vehicle:
    def __init__(self, vehicle_id, brand, model, price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price_per_day = price
        self.is_available = True

    def display_info(self):
        print(self.vehicle_id, self.brand, self.model, self.rental_price_per_day, self.is_available)

    def rent(self):
        self.is_available = False

    def return_vehicle(self):
        self.is_available = True

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days