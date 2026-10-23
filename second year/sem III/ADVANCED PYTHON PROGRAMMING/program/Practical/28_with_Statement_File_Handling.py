# Program: with Statement File Handling
# Question: What is the benefit of using the with statement for file handling in Python? Show with a
# program.

# with statement closes the file automatically (calls __exit__()) even if an exception
# occurs, so a file handler is never left open. It replaces try-finally.
with open("demo.txt", "w") as f:
    f.write("sangola\nMahavidyalaya")
print("operation successful")

with open("demo.txt", "r") as f:
    s = f.read()
print(s)

with open("demo.txt", "r") as f:
    for x in f:
        print(x)
