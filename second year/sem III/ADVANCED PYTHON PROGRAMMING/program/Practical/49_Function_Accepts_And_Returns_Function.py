# Program: Function Accepts And Returns Function
# Question: Write a python function which accepts another function as an argument as well as returns
# another function from its definition.

def add(a, b):
    return a + b

def operate(func):                 # accepts a function as argument
    def inner(x, y):               # returns another function
        print("Inner function called")
        return func(x, y)
    return inner

new_func = operate(add)
print("Result:", new_func(10, 20))
