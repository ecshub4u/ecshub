# Program: Arbitrary Arguments *args
# Question: What is arbitrary argument (*args)? Write a program of it.

# *args is used when we do not know how many arguments will be passed.
# The function receives them as a tuple.
def fun(*x):
    print(x)
    print("element", x[2])

fun("Sangola", "Solapur", "Sangli")
