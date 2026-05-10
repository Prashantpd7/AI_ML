# Problem Statement: Write a Python program to create a Rectangle class with length and width as instance attributes, and two methods: area() that returns the area and perimeter() that returns the perimeter.

# Purpose: Learn how to add instance methods to a class. Methods allow objects to perform operations using their own data, which is a key principle of encapsulation in OOP. Calculating geometric properties is a clean, practical context for understanding how self connects methods to instance data.

# Given Input: rect = Rectangle(10, 4)

# Expected Output: Area = 40 and Perimeter = 28

class Rectangle:
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def area(self):
        print("Area of Rectangle is:",self.lenght*self.width)

    def perimeter(self):
        print("Perimeter of Rectangle is:",2*self.lenght+self.width)

r1 = Rectangle(4,8)
r1.area()
r1.perimeter()