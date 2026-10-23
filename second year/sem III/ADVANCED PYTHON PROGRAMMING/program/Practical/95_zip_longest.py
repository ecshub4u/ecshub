# Program: zip_longest
# Question: Write a program to demonstrate zip_longest() of itertools.

import itertools

print(list(itertools.zip_longest("sang", "ola", fillvalue="_")))
