# Program: Filter Numbers Greater Than 18
# Question: Consider a list x = [17, 19, 15, 3, 45]. Write a python program by using filter()
# function, to extract and print numbers from above list which are greater than 18.

x = [17, 19, 15, 3, 45]

def find(n):
    return n > 18

y = filter(find, x)
print(list(y))
