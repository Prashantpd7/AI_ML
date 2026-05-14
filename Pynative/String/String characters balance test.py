# Practice Problem: Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in s1 are present in s2. The character’s position doesn’t matter.

# Exercise Purpose: This exercise focuses on membership testing. This fundamental concept is utilized in data validation, such as verifying whether a password contains required characters or determining if a search query matches a database entry.

# Given Input:

# Case 1: s1 = "yn", s2 = "PyNative"
# Case 2: s1 = "ynf", s2 = "PyNative"

# Expected Output:

# Case 1: True
# Case 2: False

def string_balance(s1,s2):
    Flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            Flag = False
            break

    return Flag

s1 = "yN"
s2 = "PyNative"
print(string_balance(s1,s2))

s1 = "ynf"
s2 = "PyNative"
print(string_balance(s1,s2))