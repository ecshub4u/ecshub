# Q10. Create an Excel spreadsheet and write Roll No. and Name data (From Professor's Notes)
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

data = [
    ["Roll No.", "Name"],
    [1, "A"],
    [2, "B"],
    [3, "C"]
]
for row in data:
    ws.append(row)

wb.save("student.xlsx")
print("Excel sheet created successfully")
