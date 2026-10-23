# Program: Create Admitted Students Spreadsheet
# Question: Write a program to create the following spreadsheet (Year, admitted students: 2022 700,
# 2023 720, 2024 735, 2025 840).

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Admissions"

data = [
    ["Year", "admitted students"],
    [2022, 700],
    [2023, 720],
    [2024, 735],
    [2025, 840],
]
for row in data:
    ws.append(row)

wb.save("admissions.xlsx")
print("admissions.xlsx created")
