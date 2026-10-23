# Q6. Read JSON file and convert it into dict object using json.load() (From Professor's Notes)
import json

with open("new.json", "r") as f:
    r = json.load(f)
print(r)
print(type(r))
