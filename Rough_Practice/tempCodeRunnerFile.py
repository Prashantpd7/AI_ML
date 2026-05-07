num = [1,2,3,4,5,6]
result = list(filter(lambda x : x % 2 == 0, num))
print(result)

num_1 = [1,2,3,4,5,6]
result_1 = list(filter(lambda x : x % 2 != 0, num_1))
print(result_1)

num_2 = [10,25,30,5,60]
result_2 = list(filter(lambda x : x > 20, num_2))
print(result_2)