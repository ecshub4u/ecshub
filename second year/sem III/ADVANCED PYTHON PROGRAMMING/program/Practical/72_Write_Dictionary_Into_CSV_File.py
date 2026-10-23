# Program: Write Dictionary Into CSV File
# Question: Write a program to write a dictionary into a CSV file.

import csv

data = [
    {"empid": 101, "Name": "ABC"},
    {"empid": 102, "Name": "PQR"},
]
fields = ["empid", "Name"]

with open("employees.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
print("employees.csv created")
