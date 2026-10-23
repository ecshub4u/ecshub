# Program: List Comprehension Demo
# Question: Write a program to demonstrate list comprehension.

marks = [10, 20, 30, 40, 50]
new = [x + 5 for x in marks]
print(new)
print(type(new))

even = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers:", even)
