# Program: pickle dumps Only Convert Object To Bytes
# Question: Write a python which only converts object into byte stream by using pickle module.
# (Assignment-2 Q.3)

import pickle

data = {"name": "abc", "place": "sangola"}
byte_stream = pickle.dumps(data)
print(byte_stream)
print(type(byte_stream))

