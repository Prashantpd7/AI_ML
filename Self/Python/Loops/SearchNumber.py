list = (1,4,9,6,8,34,76,98,35,78,56)
x = int(input("Enter number: "))
n = 0
while n<len(list):
    if (x==list[n]):
        print(n)
    n+=1