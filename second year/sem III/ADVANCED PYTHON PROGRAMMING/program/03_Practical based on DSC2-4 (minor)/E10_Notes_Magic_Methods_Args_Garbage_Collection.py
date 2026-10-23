# 1. Magic Methods (From Professor's Notes)
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Addition is", self.x + self.y)

b = A(21, 42)

num = 10
res = num.__add__(5)
print("__add__ result:", res)

# 2. Arbitrary Arguments *args (From Professor's Notes)
def fun(*x):
    print(x)
    print("element", x[2])

fun("Sangola", "Solapur", "Sangli")

# 3. Manual Garbage Collection (From Professor's Notes)
import gc
p = 10
q = 10
print(id(p))
p = 20
gc.collect()
print(id(p))
