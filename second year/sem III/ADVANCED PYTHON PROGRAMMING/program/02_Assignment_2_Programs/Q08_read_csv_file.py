# Q8. Read above CSV file and display all records on screen using csv.reader() (From Professor's Notes)
import csv

with open('democs.csv', 'r') as f:
    r = csv.reader(f)
    # extracts the first row as column headers
    header = next(r)
    print("Header:", header)
    # Iterate and print each data row
    for row in r:
        print("Data Row:", row)
