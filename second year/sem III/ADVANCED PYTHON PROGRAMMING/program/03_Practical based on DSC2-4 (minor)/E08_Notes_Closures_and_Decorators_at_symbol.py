# 1. Closure Example (From Professor's Notes)
def fun1(x):
    def fun2(y):
        return x + y
    return fun2

closure = fun1(10)
print("Closure output:", closure(5))

# 2. @ Symbol With Decorator (From Professor's Notes)
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()
