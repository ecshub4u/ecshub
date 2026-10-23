# Program: Five itertools Functions
# Question: Write a program to demonstrate any five itertools functions.

import itertools

print("count      :", list(itertools.islice(itertools.count(5, 5), 5)))
print("repeat     :", list(itertools.repeat(25, 3)))
print("accumulate :", list(itertools.accumulate([1, 2, 3, 4])))
print("chain      :", list(itertools.chain("AB", [1, 2])))
print("permutations:", list(itertools.permutations("AB", 2)))
print("combinations:", list(itertools.combinations("ABC", 2)))
print("product    :", list(itertools.product([1, 2], [3, 4])))
