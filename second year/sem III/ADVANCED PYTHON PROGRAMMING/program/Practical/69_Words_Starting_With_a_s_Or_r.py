# Program: Words Starting With a s Or r
# Question: Write a Python program to find all words starting with 'a' or 's' or 'r' in a given
# string.

import re

s = "a rain started and she ran across the road to see Ram and Sita"
words = re.findall(r"\b[asrASR]\w*", s)
print("String:", s)
print("Words starting with a, s or r:", words)
