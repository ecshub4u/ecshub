# Program: Map Add Two Lists
# Question: Write a program to add two lists using map() and lambda.

a = [1, 2]
b = [3, 4]
result = map(lambda x, y: x + y, a, b)
print(list(result))
