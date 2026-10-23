# Program: Create Excel Spreadsheet And Write Data
# Question: Write a python program to create an excel spreadsheet and write the following data into
# that sheet (Roll No., Name: 1 A, 2 B, 3 C).

# pip install openpyxl
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Students"

ws.append(["Roll No.", "Name"])
ws.append([1, "A"])
ws.append([2, "B"])
ws.append([3, "C"])

wb.save("students.xlsx")
print("students.xlsx created")
