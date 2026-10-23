# Demonstrate findall(), split(), sub(), and search() in RegEx (From Professor's Notes)
import re

# 1. re.findall()
str1 = 'hello 12 hi 89. Howdy 34'
print("findall():", re.findall(r'\d+', str1))

# 2. re.split()
str2 = 'Twelve:12 Eighty nine:89.'
print("split():", re.split(r'\d+', str2))

# 3. re.sub()
str3 = 'abc 12 de 23 f45 6'
print("sub():", re.sub(r'\s+', '', str3))

# 4. re.search()
str4 = "Python is fun"
match = re.search(r'\APython', str4)
if match:
    print("search(): pattern found inside the string")
else:
    print("search(): pattern not found")
