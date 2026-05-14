# Practice Problem: Check if a given URL starts with “https” and ends with “.com”.

# Exercise Purpose: This exercise teaches Boolean Validation. Methods like .startswith() and .endswith() are cleaner and less error-prone than manual slicing for verifying file formats, protocols, or naming conventions.

# Given Input: str1 = "https://google.com"

# Expected Output: Is valid URL: True


def url(str1):
    if str1.startswith("https") and str1.endswith(".com"):
        return True
    else:
        return False

print(url("https://google.com"))


