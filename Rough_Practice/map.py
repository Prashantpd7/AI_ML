# Given [1,2,3,4] → make all elements double.
# Given [1,2,3,4] → make all elements square.
# Given ["a","b","c"] → convert all to uppercase.
# Given [1,2,3,4] → add 10 to each element.
# Given [5,10,15] → convert each into string.


num = [1,2,3,4]
double = list(map(lambda x : x * 2, num ))
print(double)

num_1 = [1,2,3,4]
square = list(map(lambda x : x * x, num_1))
print(square)

name = ["a","b","c"]
up = list(map(lambda x : x.upper(), name))
print(up)

ele = [1,2,3,4]
add = list(map(lambda x : x + 10, ele))
print(add)

conv = [5,10,15]
converted = list(map(lambda x : str(x), conv))
print(converted)