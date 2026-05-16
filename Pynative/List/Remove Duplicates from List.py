# Practice Problem: Remove all duplicate values from a list while keeping only one instance of each element.

# Exercise Purpose: This exercise introduces Set Theory. In programming, you often need to ensure uniqueness (e.g., a list of unique email subscribers). While there are many ways to do this, using Python’s set or dict structures is the fastest way to handle the logic.

# Given Input: List: [10, 20, 10, 30, 40, 40, 20, 50]

# Expected Output: Unique List: [10, 20, 30, 40, 50]

lst = [10, 20, 10, 30, 40, 40, 20, 50]

new_lst = list(dict.fromkeys(lst))
print(new_lst)