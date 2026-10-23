# Program: Dictionary Comprehension Demo
# Question: Write a program to demonstrate dictionary comprehension.

num = [1, 2, 3, 4, 5]
new = {n: n ** 2 for n in num}
print(new)
print(type(new))
