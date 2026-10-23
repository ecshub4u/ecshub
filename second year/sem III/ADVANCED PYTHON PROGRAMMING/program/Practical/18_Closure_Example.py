# Program: Closure Example
# Question: Explain the concept of closures in Python with an example.

# A closure is a nested function that remembers the variables of the outer function
# even after the outer function has finished execution.
def fun1(x):
    def fun2(y):
        return x + y        # x is captured from the outer function
    return fun2

closure = fun1(10)
print(closure(5))
