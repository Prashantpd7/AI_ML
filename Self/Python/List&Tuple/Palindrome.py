""" Check if the input is pelindrome or not"""
list = [1, 2, 3, 2, 1]
copy_list = list.copy()
copy_list.reverse()

if (copy_list == list):
    print("Pelindrome")
else:
    print("Not a Pelindrome")

