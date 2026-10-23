# Program: Generator Prime Numbers Up To Limit
# Question: Write a Python program using a generator to yield all prime numbers up to a given limit.

def primes(limit):
    for n in range(2, limit + 1):
        flag = True
        for i in range(2, n):
            if n % i == 0:
                flag = False
                break
        if flag:
            yield n                      # yield makes this function a generator

limit = int(input("Enter limit: "))
for p in primes(limit):
    print(p, end=" ")
