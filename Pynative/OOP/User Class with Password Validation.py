# Problem Statement: Write a Python program to create a User class that stores a username and a password. Add a check_password(input_password) method that returns True if the input matches the stored password, and False otherwise.

# Purpose: This exercise introduces the idea of controlled access to sensitive data inside a class. Rather than exposing the password directly, the class provides a dedicated method to verify it. This pattern reflects a core principle of encapsulation in OOP, where internal data is protected and accessed only through defined interfaces.

# Given Input: u1 = User("alice", "secure123")

# Expected Output:

# True
# False

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        if input_password == self.password:
            return True
        else:
            return False

u1 = User("Sahil","Sahil@001")
print(u1.check_password("asdhfaskd"))
print(u1.check_password("Sahil@001"))

