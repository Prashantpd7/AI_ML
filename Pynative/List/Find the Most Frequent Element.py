# Practice Problem: Create a script that identifies the “Mode” of a list—the element that appears most frequently. If there is a tie, returning one of the top elements is sufficient for this exercise.

# Exercise Purpose: Finding the mode is a fundamental task in data science and statistics. This exercise introduces Frequency Mapping using dictionaries, a vital pattern for counting occurrences in any programming language.

# Given Input: List: [1, 3, 3, 2, 1, 1, 4, 3, 3]

# Expected Output: Mode: 3

lst = [1, 3, 3, 2, 1, 1, 4, 3, 3]

def find_mode(arr):
    frequency = {}
    
    # Count occurrences of each element
    for item in arr:
        frequency[item] = frequency.get(item, 0) + 1
    
    # Find the key with the maximum value
    mode = max(frequency, key=frequency.get)
    return mode

# Test the function
data = [1, 3, 3, 2, 1, 1, 4, 3, 3]
result = find_mode(data)
print(f"List: {data}")
print(f"Mode: {result}")