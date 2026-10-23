# Q15. Make chunks of size 3 of list [1,2,3,4,5] using batched() (From Professor's Notes)
from itertools import batched

data = [1, 2, 3, 4, 5]
# Create batches of size 3
for batch in batched(data, 3):
    print(batch)
