# Program: Filter Divisible By 3 In Reverse
# Question: Write a program to print numbers which are divisible by 3 in a range 10 to 50 in reverse
# manner by using filter function.

def div_by_3(n):
    return n % 3 == 0

y = filter(div_by_3, range(10, 51))
p = list(y)
p.reverse()                 # reverse manner
print(p)
