# Square all numbers
# Input: [1,2,3,4]
# Create a new list with squares

a = [1,2,3,4]
result = [x*x for x in a ]
print(result)

# 2) Add a constant to each element

# Input: [1,2,3]
# 👉 Add 10 to every element

b = [1,2,3]
b1 = [x+10 for x in b]
print(b1)

# 3) Convert numbers to strings

# Input: [1,2,3]
# 👉 Convert all elements to "1","2","3"

b = [1,2,3]
b1 = [str(x) for x in b]
print(b1)

# 4) Filter even numbers

# Input: [1,2,3,4,5,6]
# 👉 Keep only even numbers

c = [1,2,3,4,5,6]
c1 = [x for x in c if x % 2 == 0]
print(c1)

# 5) Filter numbers greater than a value

# Input: [5,10,15,20]
# 👉 Keep numbers greater than 10

d = [5,10,15,20]
d1 = [x for x in d if x > 10]
print(d1)

# 6) Replace values using condition (VERY IMPORTANT)

# Input: [1,2,3,4]
# 👉 Replace even → "even", odd → "odd"

e = [1,2,3,4]
e1 = [str(x) if x % 2 == 0 else str(x) for x in e ]
print(e1)

# 7) Replace only some values

# Input: [1,2,3,4]
# 👉 Replace even numbers with 0, keep others same

e = [1,2,3,4]
e1 = [ 0 if x % 2 == 0 else x for x in e ]
print(e1)


# 8) Work with strings (length filter)

# Input: ["ram","a","shyam","b"]
# 👉 Keep strings with length > 2

f = ["ram","a","shyam","b"]
f1 = [ x for x in f if len(x) > 2 ]
print(f1)


# 9) Remove falsy values (VERY IMPORTANT)

# Input: [0,1,2,"",None,3]
# 👉 Remove empty/false values

g = [0,1,2,"",None,3]
g1 = [ x for x in g if x ]
print(g1)


# 10) Flatten a nested list (IMPORTANT)

# Input: [[1,2],[3,4],[5,6]]
# 👉 Convert into [1,2,3,4,5,6]

h = [[1,2],[3,4],[5,6]]
h1 = [ j for i in h for j in i ]
print(h1)