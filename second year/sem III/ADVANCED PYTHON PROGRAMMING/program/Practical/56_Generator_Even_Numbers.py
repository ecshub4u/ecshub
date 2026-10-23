# Program: Generator Even Numbers
# Question: Write a generator which yields even numbers up to a given limit.

def even(n):
    count = 1
    while count <= n:
        if count % 2 == 0:
            yield count
        count += 1

for num in even(20):
    print(num, end=" ")
