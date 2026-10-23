# Program: Deep Copy
# Question: Write a program to create a new object which copies all nested objects within the original
# elements.

import copy

# Deep copy: new object and recursively copies all nested objects
list1 = [1, [100, 200], 3]
list2 = copy.deepcopy(list1)

print("Old List before:", list1)
list1[1][0] = 4
print("Old List:", list1)
print("New List:", list2)       # unaffected by change in the original
