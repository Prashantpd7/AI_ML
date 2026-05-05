# Create a program that takes an integer and prints its multiplication table from 1 to 10.

n = int(input("Enter number: "))
a = 1
for i in range(n):
    a*=i

print(a)