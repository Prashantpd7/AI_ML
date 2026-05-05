list = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter numbers to search: "))
n = 0
for i in list:
    if (i==x):
        print("Found at index",n)
    n += 1