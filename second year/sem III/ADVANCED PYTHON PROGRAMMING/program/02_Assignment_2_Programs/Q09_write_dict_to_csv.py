# Q9. Write a dictionary into a CSV file using csv.DictWriter() (From Professor's Notes)
import csv

data = [
    {"empid": 101, "Name": "ABC"},
    {"empid": 102, "Name": "PQR"}
]
fields = ["empid", "Name"]

with open("new.csv", 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
print("Dictionary written to CSV file successfully")
