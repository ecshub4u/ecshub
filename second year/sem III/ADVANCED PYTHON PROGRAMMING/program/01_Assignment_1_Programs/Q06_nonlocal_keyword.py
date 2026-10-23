# Q6. Demonstrate nonlocal keyword (From Professor's Notes)
def show():
    x = 10
    print("x in show:", x)
    def inner():
        nonlocal x
        x = 20
        print("x in inner:", x)
    inner()  # call to inner function

show()  # call to show function
