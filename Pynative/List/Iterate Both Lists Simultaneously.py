# Practice Problem: Use the zip() function to loop through two lists at once and print their values as pairs.

# Exercise Purpose: Iterating through two lists with a single index variable is error-prone (you might hit an “Index Out of Range” if lists are different sizes). zip() is the Safe Parallel Iterator. It stops automatically at the end of the shortest list, preventing crashes.

# Given Input:

# List 1: [10, 20, 30]
# List 2: [100, 200, 300]
# Expected Output:

# 10 100
# 20 200
# 30 300

lst = [10, 20, 30]
lst2 = [100, 200, 300]


for i, j in zip(lst,lst2):
    print(i,j)
