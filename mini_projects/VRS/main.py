from RentalService import RentalService
from Car import Car
from Bike import Bike
from Customer import Customer

service = RentalService()

# Vehicles
v1 = Bike("B101", "Honda", "CG125", 1000, "125cc", "Standard")
v2 = Car("C201", "Toyota", "Corolla", 4000, 4, "Petrol")
v3 = Car("C301", "Honda", "Civic", 6000, 4, "Petrol")

service.add_vehicle(v1)
service.add_vehicle(v2)
service.add_vehicle(v3)

# Customer
c1 = Customer("CU1", "Ali")
service.register_customer(c1)

while True:
    print("\n1. Show Vehicles")
    print("2. Rent Vehicle")
    print("3. Return Vehicle")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        service.show_available_vehicles()

    elif choice == "2":
        vid = input("Enter vehicle ID: ")
        days = int(input("Enter days: "))
        service.rent_vehicle("CU1", vid, days)

    elif choice == "3":
        service.return_vehicle("CU1")

    elif choice == "4":
        break