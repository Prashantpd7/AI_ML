# Write a lambda to add two numbers.
# Write a lambda to find square of a number.
# Write a lambda to check if a number is even or odd (return True/False).
# Write a lambda to find maximum of two numbers.
# Write a lambda to convert a string to uppercase.

add = lambda x,y : x + y
print(add(4,5))

square = lambda x : x * x
print(square(5))

check = lambda x : True if x % 2 == 0 else False
print(check(5))

find = lambda x , y : x if x > y else y
print(find(4,7))

var = lambda n : n.upper()
print(var("hello"))