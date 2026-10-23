# Q4. Convert dict object into JSON string using json.dumps() (From Professor's Notes)
import json

d = {
    "id": 101,
    "name": "Abc",
    "place": "Sangola"
}
r = json.dumps(d, indent=4)
print(r)
print(type(r))
