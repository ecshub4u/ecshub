# Program: count cycle repeat
# Question: Write python program to demonstrate a) count() b) cycle() c) repeat().

import itertools

# a) count(start, step)
print("count():")
for i in itertools.count(5, 5):
    if i > 35:
        break
    print(i, end=" ")

# b) cycle(iterable)
print("\n\ncycle():")
c = 0
for i in itertools.cycle("AB"):
    if c > 7:
        break
    print(i, end=" ")
    c += 1

# c) repeat(value, times)
print("\n\nrepeat():")
print(list(itertools.repeat(25, 4)))
