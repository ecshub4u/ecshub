# Generator to yield all prime numbers up to a given limit
def prime_generator(limit):
    num = 2
    while num <= limit:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

for p in prime_generator(20):
    print(p)
