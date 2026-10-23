# Program: Append Key Value To Existing JSON File
# Question: Write a Python program to append new key-value pairs to an existing JSON file.

# Setup: an existing JSON file
import json
with open("data.json", "w") as f:
    json.dump({"id": 101, "name": "Abc"}, f)

# Keep a JSON file named data.json in the same folder, e.g. {"id": 101, "name": "Abc"}
import json

with open("data.json", "r") as f:        # json.load() -> file to dict
    d = json.load(f)

d["place"] = "Sangola"                   # append new key-value pairs
d["course"] = "B.Sc.ECS"

with open("data.json", "w") as f:        # json.dump() -> dict to file
    json.dump(d, f)

print(d)
