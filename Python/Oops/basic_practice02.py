# Question 2: Rectangle Class
# Problem:

# Ek Rectangle class banao:

# Attributes:
# length
# width

# Methods:
# area() → area calculate kare
# perimeter() → perimeter calculate kare

class Rectange:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        Area = self.length * self.width
        print(Area)

    def perimeter(self):
        Sum = self.length + self.width
        Perimeter = 2*Sum
        print(Perimeter)

r1 = Rectange(6, 4)
r1.area()
r1.perimeter()