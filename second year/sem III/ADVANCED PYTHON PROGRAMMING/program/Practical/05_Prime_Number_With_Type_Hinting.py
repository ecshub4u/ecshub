# Program: Prime Number With Type Hinting
# Question: Write a python function to find given number is prime or not. (Use type hinting)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num: int = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
