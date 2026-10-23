# Program: Factorial Using Recursion
# Question: Write a program to find factorial of a number using recursion.

def fact(n):
    if n <= 1:                # base case
        return 1
    else:
        return n * fact(n - 1)    # recursive call

num = int(input("Enter number: "))
print("Factorial is", fact(num))
