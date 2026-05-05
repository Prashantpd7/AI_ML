def natural_num(n):
    if (n==0):
        return 0
    return natural_num(n-1) + n

sum = natural_num(5)
print(sum)