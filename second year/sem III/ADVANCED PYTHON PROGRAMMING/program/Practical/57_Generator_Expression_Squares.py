# Program: Generator Expression Squares
# Question: Write a generator expression to print squares of numbers 1 to 5.

squares = (x * x for x in range(1, 6))
print(list(squares))
