# Program: compress
# Question: Write a program to demonstrate compress() of itertools.

import itertools

data = [1, 2, 3, 4, 5]
selectors = [1, 0, 1, 0, 1]      # 1 means include, 0 means exclude
filtered = itertools.compress(data, selectors)
for item in filtered:
    print(item)
