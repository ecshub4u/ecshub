# Program: Lambda And Higher Order Function
# Question: Write a program to demonstrate lambda function and higher order function.

double = lambda x: x * 2
print(double(5))

def add(a, b):
    return (a + b)

def display(func):               # higher order function
    return (func(10, 20))

print(display(add))
