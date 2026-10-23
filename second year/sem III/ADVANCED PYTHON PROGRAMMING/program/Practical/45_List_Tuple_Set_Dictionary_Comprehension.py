# Program: List Tuple Set Dictionary Comprehension
# Question: Write a program to demonstrate list, tuple, set and dictionary comprehension.

marks = [10, 20, 30, 40, 50]

print([x + 5 for x in marks])            # list
print(tuple(x + 5 for x in marks))       # tuple (type casting)
print({x + 5 for x in marks})            # set
print({n: n ** 2 for n in marks})        # dictionary
