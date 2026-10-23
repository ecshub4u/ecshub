# Program: JSON dumps dump loads load
# Question: Explain the process of serialization and deserialization of data using the json module.
# Convert dict to JSON string and file, and vice versa.

import json

d = {"id": 101, "name": "Abc", "place": "Sangola"}

# 1) dict -> JSON string
s = json.dumps(d, indent=4)
print(s, type(s))

# 2) dict -> JSON file (serialization)
with open("new.json", "w") as f:
    json.dump(d, f)

# 3) JSON string -> dict
js = json.loads('{"id": "101", "name": "Abc", "place": "Sangola"}')
print(js, type(js))

# 4) JSON file -> dict (deserialization)
with open("new.json", "r") as f:
    r = json.load(f)
print(r, type(r))
