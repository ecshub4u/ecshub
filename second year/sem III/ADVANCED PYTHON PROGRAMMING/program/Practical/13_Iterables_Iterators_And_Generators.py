# Program: Iterables Iterators And Generators
# Question: Describe the concepts of iterables, iterators and generators in Python. Provide examples
# illustrating their differences.

# Iterable : object which returns its members one at a time (list, tuple, string, set, dict)
x = [0, 1, 5]
for p in x:
    print(p)

# Iterator : object which produces next item when next() is called; got using iter()
it = iter(x)
print(next(it))
print(next(it))
print(next(it))

# Generator : function that uses yield, remembers its local variables
def count(n):
    c = 1
    while c <= n:
        yield c
        c += 1

for num in count(5):
    print(num)

# Generator expression
squares = (a * a for a in range(1, 6))
print(list(squares))
