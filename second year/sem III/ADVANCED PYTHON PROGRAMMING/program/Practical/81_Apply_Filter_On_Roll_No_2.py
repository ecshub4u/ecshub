# Program: Apply Filter On Roll No. 2
# Question: Write python program to apply filter and filter out roll no. 2 in sheet created by
# question no. 10.

# Setup: spreadsheet of Q.10 (Roll No. | Name) - skip if students.xlsx already exists
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Students"
ws.append(["Roll No.", "Name"])
ws.append([1, "A"])
ws.append([2, "B"])
ws.append([3, "C"])
wb.save("students.xlsx")

from openpyxl import load_workbook

wb = load_workbook("students.xlsx")
ws = wb.active
ws.auto_filter.ref = "A1:B4"
ws.auto_filter.add_filter_column(0, ["2"])     # column 0 = Roll No. -> Roll No. 2
wb.save("students.xlsx")
print("Filter applied (open the file in Excel to see the result)")
