# Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.
a = 0
n = int(input("Enter number: "))
for i in range(n+1):
    a += i

print("Sum is:",a)
