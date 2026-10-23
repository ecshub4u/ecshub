# Program: Temperature Difference Using pairwise
# Question: Consider a list of temperature of a week in degree celsius [42,46,41,42,44]. Find the
# temperature difference of each next day with its previous day by using appropriate Terminating
# iterator category.

import itertools

temperatures = [42, 46, 41, 42, 44]
differences = [(b - a) for a, b in itertools.pairwise(temperatures)]
print(differences)
