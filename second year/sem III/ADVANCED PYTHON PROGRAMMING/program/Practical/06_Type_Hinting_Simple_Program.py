# Program: Type Hinting Simple Program
# Question: What is type hinting? Write a simple program of it.

# Type hints are optional annotations that declare the type of a variable / function.
# They help to catch errors before runtime. Python is still dynamically typed.
def add(x: int, y: int) -> int:
    return x + y

a: int = 20
b: int = 30
print(add(a, b))
