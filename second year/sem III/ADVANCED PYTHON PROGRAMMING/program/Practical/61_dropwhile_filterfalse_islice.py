# Program: dropwhile filterfalse islice
# Question: Write python program to demonstrate a) dropwhile() b) filterfalse() c) islice().

import itertools

# a) dropwhile() - drops elements while condition is True
data = [1, 12, 3, 5, 6, 7]
print("dropwhile():", list(itertools.dropwhile(lambda x: x < 5, data)))

# b) filterfalse() - keeps elements for which the predicate is False
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("filterfalse():", list(itertools.filterfalse(lambda n: n % 2 == 0, numbers)))

# c) islice() - slice of an iterable (start, stop, step)
print("islice():", list(itertools.islice(range(20), 0, 7, 3)))
