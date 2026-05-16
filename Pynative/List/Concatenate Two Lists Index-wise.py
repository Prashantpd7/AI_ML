# Practice Problem: Given two lists of strings, combine them index-by-index to form a single list of concatenated strings.

# Exercise Purpose: Data is often stored in parallel lists (e.g., First Names and Last Names). This exercise teaches you how to merge parallel data into a usable format, a common need for report generation and UI display.

# Given Input:

# List 1: ["Py", "is", "awes"]
# List 2: ["thon", " ", "ome"]
# Expected Output: Merged: ['Python', 'is ', 'awesome']

lst = ["Py", "is", "awes"]
lst2 = ["thon", " ", "ome"]

new_lst = []

for i in range(len(lst)):
    new_lst.append(lst[i] + lst2[i])

print(new_lst)