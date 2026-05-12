# Practice Problem: Write a program to find the last index of the substring “Emma” in a given string.

# Exercise Purpose: While the .find() method searches from the beginning of a string, the .rfind() method (Reverse Find) locates the most recent occurrence of a specified pattern. This functionality is essential when parsing file paths or URLs that require identification of the final delimiter.

# Given Input: str1 = "Emma is a data scientist who knows Python. Emma works at google."

# Expected Output: Last occurrence of Emma starts at index 43

str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Original String is:", str1)

last_str = str1.rfind("Emma")
print(last_str)