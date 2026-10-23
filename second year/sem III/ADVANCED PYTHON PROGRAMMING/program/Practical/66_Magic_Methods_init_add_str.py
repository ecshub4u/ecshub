# Program: Magic Methods init add str
# Question: Write a program to demonstrate magic methods __init__, __add__ and __str__.

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Addition is", self.x + self.y)

b = A(21, 42)

num = 10
res = num.__add__(5)
print(res)

num = 12
val = int.__str__(num)
print(type(val))
