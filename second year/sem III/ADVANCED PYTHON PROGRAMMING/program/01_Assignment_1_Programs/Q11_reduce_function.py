# Q11. Demonstrate reduce function (From Professor's Notes)
from functools import reduce

# Function to add two numbers
def add(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
res = reduce(add, a)
print(res)

# Using reduce() with lambda
res_lambda = reduce(lambda x, y: x + y, a)
print(res_lambda)
