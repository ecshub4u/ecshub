# Use map() to convert a list of temperatures from Celsius to Fahrenheit
celsius = [0, 20, 30, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))
