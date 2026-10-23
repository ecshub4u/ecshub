# Program: count() With Break Condition
# Question: Use count() to generate number sequence with break condition.

import itertools

for i in itertools.count(5, 5):          # count(start, step)
    if i == 35:
        break
    else:
        print(i, end=" ")
