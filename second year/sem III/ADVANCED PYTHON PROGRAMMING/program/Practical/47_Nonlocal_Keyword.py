# Program: Nonlocal Keyword
# Question: Write a python program to demonstrate nonlocal keyword.

def outer():
    x = 10
    print("x in outer (before):", x)

    def inner():
        nonlocal x      # refers to x of the enclosing function outer()
        x = 20
        print("x in inner         :", x)

    inner()
    print("x in outer (after) :", x)

outer()
