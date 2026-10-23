# Extract all even numbers from a list of integers using filter() and lambda
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = filter(lambda n: n % 2 == 0, x)
p = list(y)
print(p)
