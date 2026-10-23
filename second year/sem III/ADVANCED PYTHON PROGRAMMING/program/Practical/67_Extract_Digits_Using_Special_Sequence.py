# Program: Extract Digits Using Special Sequence
# Question: Write a regex pattern by using special sequence to extract only digits from input.

import re

str = input("Enter a string: ")
pattern = r"\d+"                 # \d = decimal digit
r = re.findall(pattern, str)
print(r)
