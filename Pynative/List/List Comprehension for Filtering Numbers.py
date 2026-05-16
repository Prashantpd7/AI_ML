# Practice Problem: Given a list of integers, use list comprehension to create a new list that contains only the even numbers from the original list.

# Exercise Purpose: This is the “Filter” part of the Map-Filter-Reduce paradigm. Here we focuses on Conditional Logic within a single line. It is the gold standard for creating subsets of data based on specific criteria.

# Given Input: List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Expected Output: Even Numbers: [2, 4, 6, 8, 10]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_lst = [i for i in lst if i%2==0]
print(new_lst)