# 1. Custom Iterator with Class (From Professor's Notes)
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
print("Custom Iterator:")
for num in counter:
    print(num, end=" ")
print()

# 2. Basic Generator Function using yield (From Professor's Notes)
def count(n):
    c = 1
    while c <= n:
        yield c
        c += 1

print("Generator:")
for num in count(5):
    print(num, end=" ")
print()

# 3. Recursive Function (From Professor's Notes)
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

print("Recursion:")
countdown(3)
