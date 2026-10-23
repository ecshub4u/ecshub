# Program: Create CSV File And Write Records
# Question: Write a python program to create a CSV file and write the following records into that file
# (Sr. No., Place: 1 Sangola, 2 Solapur, 3 Pune).

import csv

data = [
    ["Sr. No.", "Place"],
    [1, "Sangola"],
    [2, "Solapur"],
    [3, "Pune"],
]
with open("places.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
print("places.csv created")
