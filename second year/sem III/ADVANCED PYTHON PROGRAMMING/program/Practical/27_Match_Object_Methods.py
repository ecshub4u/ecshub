# Program: Match Object Methods
# Question: Write a program to demonstrate match object methods span(), group(), start(), end() and
# string.

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.group())
print(x.start())
print(x.end())
print(x.string)
