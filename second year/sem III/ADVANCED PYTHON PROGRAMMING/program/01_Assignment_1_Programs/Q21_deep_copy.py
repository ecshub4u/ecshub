# Q21. Deep Copy - creates a new object and recursively copies all nested objects (From Professor's Notes)
import copy

list1 = [1, [100, 200], 3]
list2 = copy.deepcopy(list1)
print('Old List before:', list1)
list1[1][0] = 4
print('Old List:', list1)
print('New List:', list2)
