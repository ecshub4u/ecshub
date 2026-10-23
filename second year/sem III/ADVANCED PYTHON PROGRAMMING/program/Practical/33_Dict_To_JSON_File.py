# Program: Dict To JSON File
# Question: Write a python program to write dict object to json file after Serialization by using JSON
# module.

import json

d = {"id": 101, "name": "Abc", "place": "Sangola"}
with open("new.json", "w") as f:
    json.dump(d, f)
print("Dictionary written to new.json")
