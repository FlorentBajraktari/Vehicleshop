# vehicleshop_app.py
from base_model import BaseModel

class VehicleShopApp:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_available_vehicles(self):
        print("Available Vehicles:")
        for vehicle in self.vehicles:
            if vehicle.available:
                print(vehicle)

    def find_vehicle_by_brand(self, brand):
        found_vehicles = [vehicle for vehicle in self.vehicles if vehicle.brand.lower() == brand.lower()]
        return found_vehicles

    def make_purchase(self, vehicle):
        if vehicle.available:
            vehicle.make_unavailable()
            total_price = vehicle.price + vehicle.calculate_vat()
            print(f"Congratulations! You have purchased the {vehicle.brand} {vehicle.model} for ${total_price:.2f}.")
        else:
            print(f"Sorry, the {vehicle.brand} {vehicle.model} is not available.")
