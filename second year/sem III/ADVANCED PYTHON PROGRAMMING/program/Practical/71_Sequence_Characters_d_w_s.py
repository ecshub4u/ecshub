# Program: Sequence Characters d w s
# Question: Explain the use of \d, \w and \s sequence characters in RegEx with illustrative patterns.

import re

print(re.findall(r"\d", "12abc3"))          # \d  any decimal digit [0-9]
print(re.findall(r"\w", "12&\": ;c"))      # \w  any alphanumeric character (and _)
print(re.findall(r"\s", "Python RegEx"))    # \s  any whitespace character
