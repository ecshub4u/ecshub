# Q9. Numbers divisible by 3 in range 10 to 50 in reverse manner using filter()
def div_by_3(x):
    return x % 3 == 0

y = filter(div_by_3, range(50, 9, -1))
p = list(y)
print(p)
