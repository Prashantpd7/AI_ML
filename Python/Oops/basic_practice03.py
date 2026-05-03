# Question 3: Employee Class
# Problem:

# Ek Employee class banao:

# Attributes:
# name
# salary
# Methods:
# display() → name aur salary print kare
# increase_salary(amount) → salary me amount add kare


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        Name = self.name
        Salary = self.salary
        print(Name,Salary)
    
    def increase_salary(self, amount):
        self.salary += amount
        print(self.salary)

e1 = Employee("Shashank", 20000)
e1.display()
e1.increase_salary(10000)