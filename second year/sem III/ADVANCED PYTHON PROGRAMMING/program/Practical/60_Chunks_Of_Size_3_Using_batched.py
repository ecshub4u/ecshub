# Program: Chunks Of Size 3 Using batched
# Question: Consider a list [1,2,3,4,5]. Make chunks of size 3 of above list by using a function of
# appropriate Terminating iterator category.

# batched() is a Terminating iterator (needs Python 3.12 or later)
from itertools import batched

data = [1, 2, 3, 4, 5]
for batch in batched(data, 3):
    print(batch)
