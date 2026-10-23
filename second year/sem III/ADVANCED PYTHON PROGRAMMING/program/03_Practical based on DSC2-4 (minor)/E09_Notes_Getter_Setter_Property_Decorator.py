# Getter and Setter using @property decorator (From Professor's Notes)
class A:
    def __init__(self):
        self._age = 0

    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter function
    @age.setter
    def age(self, a):
        if a < 18:
            raise ValueError("age is below criteria")
        print("setter method called")
        self._age = a

x = A()
x.age = 21
print(x.age)
