# Program: Words Less Than 5 Characters
# Question: Consider a string "I live in sangola". Write a python program to print words less than 5
# characters by using list comprehension.

s = "I live in sangola"
short_words = [w for w in s.split() if len(w) < 5]
print("String:", s)
print("Words with less than 5 characters:", short_words)
