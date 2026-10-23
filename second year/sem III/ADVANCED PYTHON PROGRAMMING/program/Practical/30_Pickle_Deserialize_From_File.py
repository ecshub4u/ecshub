# Program: Pickle Deserialize From File
# Question: Write a python program which reads byte stream from file and deserialize that byte stream
# into dictionary object by using pickle module.

# Setup: file created by the previous program
import pickle
with open("demo.bin", "wb") as f:
    pickle.dump({"name": "abc", "place": "sangola"}, f)

import pickle
with open("demo.bin", "rb") as f:        # file created by Q1
    x = pickle.load(f)

print(x)
