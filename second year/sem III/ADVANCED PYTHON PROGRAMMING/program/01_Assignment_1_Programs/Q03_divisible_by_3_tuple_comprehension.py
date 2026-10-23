# Q3. Numbers between 10 to 50 divisible by 3 using tuple comprehension (by type casting)
new = tuple(x for x in range(10, 51) if x % 3 == 0)
print(new)
print(type(new))
