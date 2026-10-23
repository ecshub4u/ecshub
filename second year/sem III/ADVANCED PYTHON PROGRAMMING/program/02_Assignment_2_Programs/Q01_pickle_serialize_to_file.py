# Q1. Serialize dictionary object into byte stream and write into a file using pickle.dump() (From Professor's Notes)
import pickle

data = {'name': 'abc', 'place': 'sangola'}
with open("demo.bin", "wb") as f:
    pickle.dump(data, f)
print("Serialization successful")
