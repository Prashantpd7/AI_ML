# Problem Statement: Write a Python program to create a BankAccount class with a balance attribute and two methods: deposit(amount) that adds funds to the balance, and withdraw(amount) that deducts funds but prevents the balance from going below zero.

# Purpose: Learn data validation and conditional logic inside instance methods. Preventing overdraw is a real-world business rule, and implementing it here teaches you how classes can enforce constraints on their own data, a core idea behind encapsulation in OOP.

# Given Input: Starting balance of 1000, deposit 500, withdraw 200, then attempt to withdraw 2000.

# Expected Output:

# Balance after deposit: 1500
# Balance after withdrawal: 1300
# Insufficient funds. Current balance: 1300

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f"Your current balance is: {self.balance}")
    
    def withdraw(self, amount):
        self.amount = amount
        if (self.balance - self.amount) >= 0:
            print(f"Your current balance is: {self.balance - self.amount}")
        else:
            print("Insufficient balance")

b1 = BankAccount(100000)
b1.withdraw(120000)