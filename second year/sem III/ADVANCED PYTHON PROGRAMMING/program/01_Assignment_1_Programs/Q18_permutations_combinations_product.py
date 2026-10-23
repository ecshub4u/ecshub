# Q18. Demonstrate Combinatoric Iterators: a) permutations() b) combinations() c) product() (From Professor's Notes)
from itertools import permutations, combinations, product

# a) permutations()
print("a) permutations():")
for item in permutations("AB", r=2):
    print(item)

# b) combinations()
print("b) combinations():")
for item in combinations(["A", "B", "C"], r=2):
    print(item)

# c) product()
print("c) product():")
for item in product([1, 2], [3, 4]):
    print(item)
