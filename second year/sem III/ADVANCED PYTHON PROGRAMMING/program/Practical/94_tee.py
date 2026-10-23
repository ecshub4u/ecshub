# Program: tee
# Question: Write a program to demonstrate tee() of itertools.

import itertools

numbers = [1, 2, 3]
result = itertools.tee(numbers, 2)
for num in result:
    print(list(num))
