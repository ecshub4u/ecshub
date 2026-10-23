# Q14. Demonstrate Terminating Iterators: a) accumulate() b) groupby() c) chain() (From Professor's Notes)
import itertools

# a) accumulate()
print("a) accumulate():")
a = [1, 2, 3, 4]
print(list(itertools.accumulate(a)))

# b) groupby()
print("b) groupby():")
L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
key_func = lambda x: x[0]
for key, group in itertools.groupby(L, key_func):
    print(key + " :", list(group))

# c) chain()
print("c) chain():")
list_1 = ["A", "B"]
list_2 = [1, 2, 3]
s = "san"
for p in itertools.chain(list_1, list_2, s):
    print(p)
