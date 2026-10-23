# Program: Shallow Copy
# Question: Write a program to create a new object and stores reference to the original elements.

import copy

# Shallow copy: new outer object, but nested objects are shared references
list1 = [1, [100, 200], 3]
list2 = copy.copy(list1)

print("Old List before:", list1)
print("IDs of outer lists differ:", id(list1) != id(list2))
list1[1][0] = 4
print("Old List:", list1)
print("New List:", list2)       # nested change is reflected in both
