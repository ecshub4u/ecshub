# Program: Reduce Function Demo
# Question: Write a python program to demonstrate reduce function.

from functools import reduce

def add(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
print("Sum using function:", reduce(add, a))
print("Sum using lambda  :", reduce(lambda x, y: x + y, a))
print("Maximum           :", reduce(lambda x, y: x if x > y else y, a))
