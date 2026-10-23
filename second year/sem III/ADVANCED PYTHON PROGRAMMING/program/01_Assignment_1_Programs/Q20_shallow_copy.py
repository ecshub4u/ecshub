# Q20. Shallow Copy - creates a new object and stores reference to the original elements (From Professor's Notes)
import copy

list1 = [1, 2, 3]
list2 = copy.copy(list1)
list1[1] = 4
print('Old List:', list1)
print('New List:', list2)

# Nested list shallow copy example from notes
list1 = [1, [100, 200], 3]
list2 = copy.copy(list1)
print('Old List before:', list1)
list1[1][0] = 4
print('Old List:', list1)
print('New List:', list2)
