# Program: Decorator With And Without @ Symbol
# Question: Write a program to demonstrate decorators.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

decorated_func = make_pretty(ordinary)      # without @
decorated_func()

@make_pretty                                # with @
def ordinary2():
    print("I am ordinary")

ordinary2()
