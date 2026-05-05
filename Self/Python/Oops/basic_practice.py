
# Problem:

# Ek Car class banao jisme:

# Attributes:
# brand
# model
# price

# Methods:
# display_info() → sab details print kare
# is_expensive() → agar price > 10 lakh ho to "Expensive" warna "Affordable"

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        a = self.brand
        b = self.model
        c = self.price
        print(a,b,c)
    
    def is_expensive(self):
        if self.price > 10:
            print("Expensive")
        else:
            print("Not expensive")


c1 = Car("mercedes", "sedan", 99)
c1.display_info()
c1.is_expensive()