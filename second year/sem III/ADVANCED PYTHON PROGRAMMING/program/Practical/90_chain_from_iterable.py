# Program: chain.from_iterable
# Question: Write a program to demonstrate chain.from_iterable().

from itertools import chain

x = chain.from_iterable(['sangola', 'Mahavidyalaya'])
# printing the flattened iterable
print(list(x))
