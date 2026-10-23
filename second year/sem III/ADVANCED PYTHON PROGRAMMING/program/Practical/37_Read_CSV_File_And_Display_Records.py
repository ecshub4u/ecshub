# Program: Read CSV File And Display Records
# Question: Write a python program to read the above CSV file and display all records on screen.

# Setup: CSV file created by the previous program
import csv
with open("places.csv", "w", newline="") as f:
    csv.writer(f).writerows([["Sr. No.", "Place"], [1, "Sangola"], [2, "Solapur"], [3, "Pune"]])

import csv
with open("places.csv", "r") as f:       # file created by Q7
    r = csv.reader(f)
    header = next(r)
    print("Header:", header)
    for row in r:
        print("Data Row:", row)
