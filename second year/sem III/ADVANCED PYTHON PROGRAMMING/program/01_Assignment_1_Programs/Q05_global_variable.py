# Q5. Program in which a variable (global variable) can be accessed everywhere in program
x = 100  # global variable

def show():
    print("x inside:", x)

show()  # call to show function
print("x outside:", x)
