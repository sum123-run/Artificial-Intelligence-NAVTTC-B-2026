class RentalService:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def register_customer(self, customer):
        self.customers.append(customer)

    def show_available_vehicles(self):
        for v in self.vehicles:
            if v.is_available:
                v.display_info()

    def rent_vehicle(self, customer_id, vehicle_id, days):
        for c in self.customers:
            if c.customer_id == customer_id:
                for v in self.vehicles:
                    if v.vehicle_id == vehicle_id and v.is_available:
                        v.rent()
                        c.rent_vehicle(v)
                        cost = v.calculate_rental_cost(days)
                        print("Total Cost:", cost)
                        return
        print("Vehicle not available")

    def return_vehicle(self, customer_id):
        for c in self.customers:
            if c.customer_id == customer_id and c.rented_vehicle:
                c.rented_vehicle.return_vehicle()
                c.return_vehicle()
                print("Vehicle returned")
                return
        print("No vehicle found")