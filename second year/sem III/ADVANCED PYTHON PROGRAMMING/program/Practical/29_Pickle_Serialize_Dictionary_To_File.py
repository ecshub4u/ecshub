# Program: Pickle Serialize Dictionary To File
# Question: Write a python program which writes byte stream into a file after serialize the dictionary
# object into byte stream by using pickle module.

import pickle

data = {"name": "abc", "place": "sangola"}
with open("demo.bin", "wb") as f:
    pickle.dump(data, f)
print("Dictionary serialized and written to demo.bin")
