# Program: Map Lambda Square Of Each Element
# Question: Write a map function by using lambda function to print square of each element present in a
# list.

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("List   :", numbers)
print("Squares:", squares)
