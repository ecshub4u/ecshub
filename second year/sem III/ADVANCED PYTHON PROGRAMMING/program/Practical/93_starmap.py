# Program: starmap
# Question: Write a program to demonstrate starmap() of itertools.

import itertools

def add(a, b):
    return a + b

pairs = [(2, 3), (4, 5)]
result = itertools.starmap(add, pairs)
for value in result:
    print(value)
