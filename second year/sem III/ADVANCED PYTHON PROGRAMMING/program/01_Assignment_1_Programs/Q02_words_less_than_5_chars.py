# Q2. Print words less than 5 characters from "I live in sangola" using list comprehension
s = "I live in sangola"
words = s.split()
new = [x for x in words if len(x) < 5]
print(new)
