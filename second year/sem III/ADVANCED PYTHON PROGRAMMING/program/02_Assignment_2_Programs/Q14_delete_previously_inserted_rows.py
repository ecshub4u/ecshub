# Q14. Delete previously inserted two rows using delete_rows() (From Professor's Notes)
from openpyxl import load_workbook

wb = load_workbook("student.xlsx")
ws = wb.active
ws.delete_rows(idx=4, amount=2)
wb.save("student.xlsx")
print("Previously inserted rows deleted")
