# Q5. Write dict object to JSON file after Serialization using json.dump() (From Professor's Notes)
import json

d = {
    "id": 101,
    "name": "Abc",
    "place": "Sangola"
}
with open("new.json", "w") as f:
    json.dump(d, f)
print("JSON file written successfully")
