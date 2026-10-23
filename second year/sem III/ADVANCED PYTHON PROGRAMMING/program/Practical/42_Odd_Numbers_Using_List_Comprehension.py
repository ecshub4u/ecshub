# Program: Odd Numbers Using List Comprehension
# Question: Write a python program to print odd numbers of a list by using list comprehension.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
odd = [x for x in numbers if x % 2 != 0]
print("Original list:", numbers)
print("Odd numbers  :", odd)
