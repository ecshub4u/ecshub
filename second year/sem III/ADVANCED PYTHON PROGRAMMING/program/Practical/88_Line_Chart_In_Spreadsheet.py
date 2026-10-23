# Program: Line Chart In Spreadsheet
# Question: Write a program to create line chart using above spreadsheet in Q.19.

from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference

wb = Workbook()
ws = wb.active
ws.title = "Admissions"
for row in [["Year", "admitted students"], [2022, 700], [2023, 720], [2024, 735], [2025, 840]]:
    ws.append(row)

chart = LineChart()
data = Reference(ws, min_col=2, min_row=1, max_row=5)         # values (with header as title)
categories = Reference(ws, min_col=1, min_row=2, max_row=5)   # years
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, "D2")
wb.save("line_chart.xlsx")
print("line_chart.xlsx created")
