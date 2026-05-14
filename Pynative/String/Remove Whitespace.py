# Practice Problem: Remove every single space from a given string, including spaces between words.

# Exercise Purpose: This highlights the difference between Trimming and Filtering. While .strip() only removes leading/trailing spaces, .replace() can reach inside a string to remove characters globally.

# Given Input: str1 = " P y t h o n "

# Expected Output: Python

str1 = " P y t h o n "

new = str1.replace(" ","")
print(new)