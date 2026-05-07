# Given [1,2,3,4,5,6] → keep only even numbers.
# Given [1,2,3,4,5,6] → keep only odd numbers.
# Given [10,25,30,5,60] → keep numbers greater than 20.
# Given ["ram","a","shyam","b"] → keep strings with length > 2.
# Given [0,1,2,"",None,3] → remove empty/false values.

num = [1,2,3,4,5,6]
result = list(filter(lambda x : x % 2 == 0, num))
print(result)

num_1 = [1,2,3,4,5,6]
result_1 = list(filter(lambda x : x % 2 != 0, num_1))
print(result_1)

num_2 = [10,25,30,5,60]
result_2 = list(filter(lambda x : x > 20, num_2))
print(result_2)

name = ["ram","a","shyam","b"]
conv = list(filter(lambda x : len(x) > 2, name))
print(conv)

value = [0,1,2,"",None,3]
final = list(filter(bool, value))
print(final)