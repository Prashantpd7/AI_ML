
# Polymorphism
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

d1 = Dog()
d1.sound()

c1 = Cat()
c1.sound()

# Abstraction

# from abc import ABC, abstractmethod

# class Shape(ABC):
    
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def area(self):
#         return 10 * 5
    
# r = Rectangle()
# print(r.area())