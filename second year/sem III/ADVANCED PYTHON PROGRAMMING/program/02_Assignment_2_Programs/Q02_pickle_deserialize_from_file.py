# Q2. Read byte stream from file and deserialize into dictionary object using pickle.load() (From Professor's Notes)
import pickle

with open("demo.bin", "rb") as f:
    x = pickle.load(f)
print(x)
