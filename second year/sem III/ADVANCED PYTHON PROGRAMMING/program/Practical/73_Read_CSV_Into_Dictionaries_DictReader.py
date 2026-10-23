# Program: Read CSV Into Dictionaries DictReader
# Question: Write a program to read a CSV file into a list of dictionaries using csv.DictReader().

import csv

data = [
    {"empid": 101, "Name": "ABC"},
    {"empid": 102, "Name": "PQR"},
]
fields = ["empid", "Name"]
with open("new.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

d = []
with open("new.csv", "r") as f:
    r = csv.DictReader(f)
    for row in r:
        d.append(row)
print(d)
