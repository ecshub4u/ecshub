# Use itertools.count() to generate number sequence with break condition (From Professor's Notes)
import itertools

for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")
