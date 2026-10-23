# Remaining itertools functions from Professor's Notes
import itertools
import re

# 1. chain.from_iterable()
x = itertools.chain.from_iterable(['sangola', 'Mahavidyalaya'])
print("chain.from_iterable:", list(x))

# 2. compress()
data = [1, 2, 3, 4, 5]
selectors = [1, 0, 1, 0, 1]
print("compress:", list(itertools.compress(data, selectors)))

# 3. starmap()
pairs = [(2, 3), (4, 5)]
print("starmap:", list(itertools.starmap(lambda a, b: a + b, pairs)))

# 4. takewhile()
numbers = [1, 4, 12, 7, 15]
print("takewhile:", list(itertools.takewhile(lambda x: x < 10, numbers)))

# 5. tee()
it1, it2 = itertools.tee([1, 2, 3], 2)
print("tee:", list(it1), list(it2))

# 6. zip_longest()
print("zip_longest:", list(itertools.zip_longest('sang', 'ola', fillvalue='_')))

# 7. combinations_with_replacement()
print("combinations_with_replacement:", list(itertools.combinations_with_replacement(['A', 'B'], 2)))

# 8. Match Object methods (.span(), .string, .group(), .start(), .end())
txt = "The rain in Spain"
m = re.search(r"\bS\w+", txt)
print("span():", m.span())
print("string:", m.string)
print("group():", m.group())
print("start():", m.start())
print("end():", m.end())
