# Practice Problem: Write a program to split a given string on hyphens and display each substring.

# Exercise Purpose: This exercise introduces the concept of tokenization. Dividing strings into smaller components based on delimiters, such as commas, spaces, or hyphens, is a common technique for processing CSV files, logs, and user-entered lists.

# Given Input: str1 = "Emma-is-a-data-scientist"

# Expected Output:

# Displaying each substring: 
# Emma
# is
# a
# data
# scientist

str1 = "Emma-is-a-data-scientist"
print(str1)

sub_strings = str1.split("-")

print(sub_strings)

for s in sub_strings:
    print(s)