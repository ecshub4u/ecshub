# Program: Create Iterator Class Counter
# Question: Write a program to create an iterator which prints elements of an iterable.

x = [0, 1, 5]            # x is an iterable
it = iter(x)             # creating iterator
print(next(it))
print(next(it))
print(next(it))

# Custom iterator using a class (__iter__ and __next__)
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

counter = Counter(1, 5)
for num in counter:
    print(num)
