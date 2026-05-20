# Practice Problem: Write a Python function that takes a list of numbers and returns the second largest value. Ensure the function handles lists with duplicate values correctly (e.g., if the list is [10, 10, 9], the second largest is 9).

# Exercise Purpose: This exercise teaches you how to process data sets where “rank” matters. It also highlights the importance of handling duplicates. Simply sorting a list does not work if the largest number appears multiple times. It introduces the concept of using Sets to make data unique.

# Given Input: List: [12, 35, 1, 10, 34, 1, 35,36,36,36,36,37,37]

# Expected Output: Second Largest: 34

lst = [12, 35, 1, 10, 34, 1, 35,38,45,45]

unique = list(set(lst))
unique.sort()
print(unique)
print(unique[-2])