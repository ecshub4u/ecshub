# Program: Recursive Function Countdown
# Question: What is Recursive function? Write a simple program of it.

# A recursive function is a function that calls itself to solve a problem
# in smaller sub-problems. It must have a base case to stop.
def countdown(n):
    if n <= 0:              # base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1)    # recursive call

countdown(3)
