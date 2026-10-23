# Q23. Extract only digits from input using special sequence \d+ (From Professor's Notes)
import re

str_val = 'hello 12 hi 89. Howdy 34'
pattern = r'\d+'
r = re.findall(pattern, str_val)
print(r)
