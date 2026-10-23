# Program: Getter Setter And property Function
# Question: Write a program to demonstrate getter and setter methods and property() function.

class A:
    def __init__(self, age=0):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, x):
        self._age = x

    age = property(get_age, set_age)

x = A()
x.set_age(21)
print(x.get_age())
x.age = 25
print(x.age)
