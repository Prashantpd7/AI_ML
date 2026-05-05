# Question 5: BankAccount Class (important)
# Problem:

# Ek BankAccount class banao:

# Attributes:
# name
# balance
# Methods:
# deposit(amount)
# withdraw(amount) (agar balance kam ho to message print karo)
# check_balance()


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Your current balance is: ",self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("Low balance")
        else:
            print("Successful")

b1 = BankAccount("Sahil",50000)
b1.deposit(10000)
b1.withdraw(70000)