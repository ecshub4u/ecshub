# Q7. Create a CSV file and write records using csv.writer() (From Professor's Notes)
import csv

data = [
    ['Sr. No.', 'Place'],
    [1, 'Sangola'],
    [2, 'Solapur'],
    [3, 'Pune']
]
with open('democs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
print("CSV file created successfully")
