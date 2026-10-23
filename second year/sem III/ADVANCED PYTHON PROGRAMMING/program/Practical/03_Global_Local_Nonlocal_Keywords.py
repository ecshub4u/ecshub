# Program: Global Local Nonlocal Keywords
# Question: Write a program to demonstrate global, local, nonlocal keywords.

x = 100                       # global variable

def show_global():
    print("Global x:", x)

def show_local():
    x = 10                    # local variable (separate from global x)
    print("Local x :", x)

def modify_global():
    global x                  # modify the global variable
    x = 200

def outer():
    y = 1
    def inner():
        nonlocal y            # modify enclosing function's variable
        y = 2
    inner()
    print("nonlocal y:", y)

show_global()
show_local()
modify_global()
print("Global x after modify_global():", x)
outer()
