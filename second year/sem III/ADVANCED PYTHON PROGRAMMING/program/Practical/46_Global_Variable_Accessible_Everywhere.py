# Program: Global Variable Accessible Everywhere
# Question: Write a python program in which a variable can be accessed everywhere in program.

# A global variable is declared outside every function, so it is accessible everywhere
x = 100          # global variable

def show():
    print("x inside function :", x)

show()
print("x outside function:", x)
