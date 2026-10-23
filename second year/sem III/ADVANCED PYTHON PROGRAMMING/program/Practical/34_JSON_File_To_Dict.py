# Program: JSON File To Dict
# Question: Write a python program to read json file and convert it into dict object by using JSON
# module.

# Setup: file created by the previous program
import json
with open("new.json", "w") as f:
    json.dump({"id": 101, "name": "Abc", "place": "Sangola"}, f)

import json
with open("new.json", "r") as f:         # file created by Q5
    r = json.load(f)
print(r)
print(type(r))
