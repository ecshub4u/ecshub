# Append new key-value pairs to an existing JSON file
import json

# Step 1: Read existing JSON file into dict using json.load()
with open("new.json", "r") as f:
    data = json.load(f)

# Step 2: Add new key-value pair to dictionary
data["college"] = "Sangola Mahavidyalaya"

# Step 3: Write updated dictionary back to JSON file using json.dump()
with open("new.json", "w") as f:
    json.dump(data, f, indent=4)

print("Updated JSON data:", data)
