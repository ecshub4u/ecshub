# Program: combinations_with_replacement
# Question: Write a program to demonstrate combinations_with_replacement().

import itertools
p = ['A', 'B']
result = itertools.combinations_with_replacement(p, 2)
for item in result:
    print(item)
