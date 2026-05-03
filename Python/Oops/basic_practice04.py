# Question 4: Mobile Class
# Problem:

# Ek Mobile class banao:

# Attributes:
# brand
# battery (in %)
# Methods:
# use_phone(hours) → battery reduce kare (1 hour = -10%)
# charge() → battery ko 100% kar de


class Mobile:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def use_phone(self, hours):
        for i in range(hours):
            self.battery -= 10
        print("Battery remaning",self.battery)

    def charge(self):
        self.battery = 100
        print("Battery fully charged",self.battery)

m1 = Mobile("Apple", 80)
m1.use_phone(3)
m1.charge()
m1.use_phone(4)