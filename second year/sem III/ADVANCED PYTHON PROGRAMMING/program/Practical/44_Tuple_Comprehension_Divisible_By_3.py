# Program: Tuple Comprehension Divisible By 3
# Question: Write a python program which prints numbers between 10 to 50 which are divisible by 3 by
# using tuple comprehension.

# Python has no direct tuple comprehension, so we pass a generator expression to tuple()
result = tuple(x for x in range(10, 51) if x % 3 == 0)
print(result)
print(type(result))
