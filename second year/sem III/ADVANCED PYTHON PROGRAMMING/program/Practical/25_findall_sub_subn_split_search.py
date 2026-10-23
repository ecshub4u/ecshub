# Program: findall sub subn split search
# Question: Write a program to demonstrate findall, sub, split, search functions in regular
# expression.

import re

text = "hello 12 hi 89. Howdy 34"

print("findall:", re.findall(r"\d+", text))
print("sub    :", re.sub(r"\s+", "", text))
print("subn   :", re.subn(r"\s+", "", text))
print("split  :", re.split(r"\d+", text))

m = re.search(r"\d+", text)
if m:
    print("search :", m.group(), "at", m.span())
