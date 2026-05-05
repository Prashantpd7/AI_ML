# File handling
# Regex --> Regular expression 


# class Demo:
#     x = 5

# d1 = Demo()
# d2 = Demo()

# d1.x = d1.x + 5

# print(d1.x)
# print(d2.x)

# class A:
#     classvar1 = "I am in class A"
#     def __init__(self):
#         self.var1 = "I am inside class A's Constructor "

# class Shape:
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         return self.length * self.breadth
    
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius

# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.base * self.height
    
# a = [Rectangle(3,4),Circle(5),Triangle(6,7)]

# for shapes in a:
#     print(shapes.area())


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def set_mileage(self,mileage):
        self.mileage = mileage
    def show_mileage(self):
        return self.mileage
    
class Car(Vehicle):
    def set_mileage(self,mileage):
        self.mileage = mileage
    def show_mileage(self):
        return self.mileage
