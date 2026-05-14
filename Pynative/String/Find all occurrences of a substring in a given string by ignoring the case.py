# Practice Problem: Write a program to find the total count of the substring “USA” in a given string, ignoring the case (i.e., both “usa” and “USA” should be counted).

# Exercise Purpose: This exercise addresses case normalization. In practical data science and web scraping applications, text data is frequently inconsistent. Converting all text to lowercase prior to processing is considered a standard best practice.

# Given Input: str1 = "Welcome to USA. usa awesome, isn't it?"

# Expected Output: The USA count is: 2

str1 = "Welcome to USA. usa awesome, isn't it?"
str01 = str1.lower()
total = str01.count("usa")
print("USA is",total,"times")