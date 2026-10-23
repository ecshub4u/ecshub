# Q7. Function accepting another function as argument and returning another function (Higher-order / Decorator)
def make_pretty(func):
    # define the inner function
    def inner():
        print("I got decorated")
        func()
    # return the inner function
    return inner

def ordinary():
    print("I am ordinary")

# pass function as argument and receive returned function
decorated_func = make_pretty(ordinary)
decorated_func()
