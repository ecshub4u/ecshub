# Q16. Apply filter on Roll No. 2 using auto_filter (From Professor's Notes)
from openpyxl import load_workbook

wb = load_workbook("student.xlsx")
ws = wb.active
ws.auto_filter.ref = "A1:B4"
ws.auto_filter.add_filter_column(0, ["2"])
wb.save("student.xlsx")
print("Filter applied successfully")
