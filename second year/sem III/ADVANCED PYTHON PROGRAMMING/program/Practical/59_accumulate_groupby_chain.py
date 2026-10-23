# Program: accumulate groupby chain
# Question: Write python program to demonstrate a) accumulate() b) groupby() c) chain().

import itertools, operator
from itertools import chain

# a) accumulate()
a = [1, 2, 3, 4, 5]
print("accumulate (sum)     :", list(itertools.accumulate(a)))
print("accumulate (multiply):", list(itertools.accumulate(a, operator.mul)))
print("accumulate (max)     :", list(itertools.accumulate([5, 3, 6, 2, 1, 9, 1], max)))

# b) groupby()
L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
print("\ngroupby():")
for key, group in itertools.groupby(L, lambda x: x[0]):
    print(key, ":", list(group))

# c) chain()
print("\nchain():")
for p in chain(["A", "B"], [1, 2, 3], "san"):
    print(p, end=" ")
print()
