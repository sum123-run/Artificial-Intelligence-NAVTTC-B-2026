class Customer:
    def __init__(self, cid, name):
        self.customer_id = cid
        self.name = name
        self.rented_vehicle = None

    def rent_vehicle(self, vehicle):
        self.rented_vehicle = vehicle

    def return_vehicle(self):
        self.rented_vehicle = None

    def view_rented_vehicle(self):
        if self.rented_vehicle:
            print("Rented:", self.rented_vehicle.vehicle_id)
        else:
            print("No vehicle rented")