# Q13. Insert two rows above Roll No. 3 (Row 4) using insert_rows() (From Professor's Notes)
from openpyxl import load_workbook

wb = load_workbook("student.xlsx")
ws = wb.active
ws.insert_rows(idx=4, amount=2)
wb.save("student.xlsx")
print("Two rows inserted above Roll No. 3")
