# Practice Problem: Given a list of numbers, create a new list where each number is replaced by its square (n2) using a single line of code.

# Exercise Purpose: This is your introduction to List Comprehensions. In Python, writing a full for loop to build a new list is often considered un-Pythonic. List comprehensions execute faster and are cleaner to read, providing a concise way to map a function across a collection.

# Given Input: List: [1, 2, 3, 4, 5]

# Expected Output: Squared List: [1, 4, 9, 16, 25]

lst = [1, 2, 3, 4, 5]

new_lst = [i*i for i in lst]

print(new_lst)