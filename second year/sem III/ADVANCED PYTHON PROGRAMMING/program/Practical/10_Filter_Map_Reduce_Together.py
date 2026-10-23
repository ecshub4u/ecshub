# Program: Filter Map Reduce Together
# Question: Write a program to demonstrate filter, map, reduce functions.

from functools import reduce

nums = [10, 19, 21, 30, 15, 5]

print("filter (>= 18):", list(filter(lambda n: n >= 18, nums)))
print("map (+5)      :", list(map(lambda n: n + 5, nums)))
print("reduce (sum)  :", reduce(lambda a, b: a + b, nums))
