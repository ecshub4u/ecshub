# Program: Dict To JSON String
# Question: Write a python program to convert dict object into json string.

import json

d = {"id": 101, "name": "Abc", "place": "Sangola"}
r = json.dumps(d, indent=4)
print(r)
print(type(r))
