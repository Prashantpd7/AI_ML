# Problem Statement: Write a Python program to create a Vehicle class with two instance attributes: max_speed and mileage. Create an object of the class and print both attributes.

# Purpose: Learn to define instance attributes using the __init__ constructor method. Instance attributes are unique to each object, meaning different Vehicle objects can hold different values for speed and mileage. This is a foundational concept in object-oriented programming.

# Given Input: vehicle1 = Vehicle("Tesla Model S", 250, 18)

# Expected Output: Vehicle Name: Tesla Model S, Speed: 250, Mileage: 18


class Vehicle:
    def __init__(self,Vehicle_Name, max_speed, mileage):
        self.Vehicle_Name = Vehicle_Name
        self.max_speed = max_speed
        self.mileage = mileage

        print(f"Vehicle Name: {self.Vehicle_Name}, Speed: {self.max_speed}, Mileage: {self.mileage}")

v1 = Vehicle("BMW",300,15)
