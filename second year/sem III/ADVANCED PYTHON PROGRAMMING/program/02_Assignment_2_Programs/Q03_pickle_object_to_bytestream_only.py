# Q3. Only convert Python object into byte stream (without file) using pickle.dumps()
import pickle

data = {'name': 'abc', 'place': 'sangola'}
byte_stream = pickle.dumps(data)
print(byte_stream)
