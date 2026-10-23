# Program: Garbage Collection
# Question: What is garbage collection in python? Show with a program.

# Garbage collection is an automated memory management process that deletes objects
# which are not in use. It can also be run manually with gc.collect().
import gc
p = 10
q = 10
print(id(p))
print(id(q))

p = 20
q = 20
gc.collect()
print(id(p))
print(id(q))
