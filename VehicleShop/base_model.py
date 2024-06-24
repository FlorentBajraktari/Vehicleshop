# base_model.py

class BaseModel:
    def __init__(self, brand, model, year, price, available=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.available = available
    
    def calculate_vat(self):
        vat_rate = 0.20  # Tarifa e TVSH (20%)
        vat_amount = self.price * vat_rate
        return vat_amount

    def __str__(self):
        return f"{self.brand} {self.model}, {self.year}, ${self.price}, VAT: ${self.calculate_vat():.2f}, Available: {self.available}"

    def make_unavailable(self):
        self.available = False
