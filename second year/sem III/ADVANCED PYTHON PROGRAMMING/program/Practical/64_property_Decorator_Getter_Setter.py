# Program: @property Decorator Getter Setter
# Question: Write a program to demonstrate @property decorator (getter and setter with validation).

class A:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        print("getter method called")
        return self._age

    @age.setter
    def age(self, a):
        if a < 18:
            raise ValueError("age is below criteria")
        print("setter method called")
        self._age = a

x = A()
x.age = 21
print(x.age)
