# Program: Mobile Number Pattern Starting 8 Or 9
# Question: Write a python program to match a pattern of a mobile number which starts from 8 or 9.

import re

pattern = r"^[89]\d{9}$"       # starts with 8 or 9, total 10 digits
numbers = ["9876543210", "8123456789", "7123456789", "98765", "98765432101"]

for n in numbers:
    if re.match(pattern, n):
        print(n, "-> valid mobile number")
    else:
        print(n, "-> invalid")
