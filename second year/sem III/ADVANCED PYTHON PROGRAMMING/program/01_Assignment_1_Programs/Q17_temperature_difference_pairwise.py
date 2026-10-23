# Q17. Find temperature difference of each next day with previous day using pairwise() (From Professor's Notes)
import itertools

temperatures = [42, 46, 41, 42, 44]
differences = [(b - a) for a, b in itertools.pairwise(temperatures)]
print(differences)
