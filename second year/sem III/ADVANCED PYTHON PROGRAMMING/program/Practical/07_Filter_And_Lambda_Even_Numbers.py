# Program: Filter And Lambda Even Numbers
# Question: Write a Python program using filter() and lambda to extract all even numbers from a list
# of integers.

x = [10, 15, 22, 7, 8, 31, 40]
y = filter(lambda n: n % 2 == 0, x)
print(list(y))
