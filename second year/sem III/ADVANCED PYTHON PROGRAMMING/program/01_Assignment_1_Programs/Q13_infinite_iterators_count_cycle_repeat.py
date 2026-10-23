# Q13. Demonstrate Infinite Iterators: a) count() b) cycle() c) repeat() (From Professor's Notes)
import itertools

# a) count(start, step)
print("a) count():")
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")
print()

# b) cycle(iterable)
print("b) cycle():")
count = 0
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end=" ")
        count += 1
print()

# c) repeat(val, num)
print("c) repeat():")
print("Printing the numbers repeatedly:")
print(list(itertools.repeat(25, 4)))
