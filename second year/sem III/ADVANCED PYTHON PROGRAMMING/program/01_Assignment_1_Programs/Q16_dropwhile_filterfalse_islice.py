# Q16. Demonstrate a) dropwhile() b) filterfalse() c) islice() (From Professor's Notes)
import itertools

# a) dropwhile()
print("a) dropwhile():")
def show(x):
    return x < 5

data = [1, 12, 3, 5, 6, 7]
result = itertools.dropwhile(show, data)
for num in result:
    print(num)

# b) filterfalse()
print("b) filterfalse():")
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = itertools.filterfalse(is_even, numbers)
for num in result:
    print(num)

# c) islice()
print("c) islice():")
numbers = range(20)
selected = itertools.islice(numbers, 0, 7, 3)
for num in selected:
    print(num)
