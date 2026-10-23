# Program: Factorial Using Reduce
# Question: Write a program to find factorial of a number using reduce().

from functools import reduce

n = 5
res = reduce(lambda x, y: x * y, range(1, n + 1))
print("Factorial of", n, "is", res)
