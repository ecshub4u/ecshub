# Program: permutations combinations product
# Question: Write python program to demonstrate a) permutations() b) combinations() c) product().

from itertools import permutations, combinations, product

print("permutations('ABC', r=2):")
for item in permutations("ABC", r=2):
    print(item)

print("\ncombinations(['A','B','C'], r=2):")
for item in combinations(["A", "B", "C"], r=2):
    print(item)

print("\nproduct([1,2],[3,4]):")
for item in product([1, 2], [3, 4]):
    print(item)
