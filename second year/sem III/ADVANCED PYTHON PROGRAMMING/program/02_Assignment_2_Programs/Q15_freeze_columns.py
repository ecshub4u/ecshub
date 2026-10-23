# Q15. Freeze column of spreadsheet using freeze_panes (From Professor's Notes)
from openpyxl import load_workbook

wb = load_workbook("student.xlsx")
ws = wb.active
ws.freeze_panes = 'B1'  # Freezes column A
wb.save("student.xlsx")
print("Column frozen successfully")
