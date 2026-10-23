# Program: takewhile
# Question: Write a program to demonstrate takewhile() of itertools.

import itertools

numbers = [1, 4, 12, 7, 15]
result = itertools.takewhile(lambda x: x < 10, numbers)
for num in result:
    print(num)
