# Q8. Find if given number is prime or not using type hinting
def check_prime(n: int) -> str:
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

num: int = 7  # type hint
print(check_prime(num))
