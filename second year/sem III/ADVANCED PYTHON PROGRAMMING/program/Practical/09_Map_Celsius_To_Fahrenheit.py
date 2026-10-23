# Program: Map Celsius To Fahrenheit
# Question: Use map() to convert a list of temperatures from Celsius to Fahrenheit.

celsius = [0, 10, 20, 30, 40]

def to_f(c):
    return c * 9 / 5 + 32

fahrenheit = list(map(to_f, celsius))
print("Celsius   :", celsius)
print("Fahrenheit:", fahrenheit)

# same using lambda
print(list(map(lambda c: c * 9 / 5 + 32, celsius)))
