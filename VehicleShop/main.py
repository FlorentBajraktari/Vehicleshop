# main.py
from vehicleshop_app import VehicleShopApp
from base_model import BaseModel

if __name__ == "__main__":
    app = VehicleShopApp()

    # Shtimi i disa makinave në aplikacion
    car1 = BaseModel("BMW", "X5", 2020, 45000)
    car2 = BaseModel("Mercedes-Benz", "C-Class", 2018, 35000)
    car3 = BaseModel("Audi", "A4", 2022, 38000)
    car4 = BaseModel("Volkswagen", "Golf", 2019, 25000)

    app.add_vehicle(car1)
    app.add_vehicle(car2)
    app.add_vehicle(car3)
    app.add_vehicle(car4)

    # Shfaqja e makinave të disponueshme
    app.display_available_vehicles()

    # Blerja e një makinë
    cars_by_brand = app.find_vehicle_by_brand("BMW")
    if cars_by_brand:
        car_to_purchase = cars_by_brand[0]  # Për qëllime demonstruese, merr makinën e parë në listë
        app.make_purchase(car_to_purchase)
    else:
        print("No BMW vehicles found.")

    # Shfaqja e makinave të disponueshme pas blerjes
    app.display_available_vehicles()
