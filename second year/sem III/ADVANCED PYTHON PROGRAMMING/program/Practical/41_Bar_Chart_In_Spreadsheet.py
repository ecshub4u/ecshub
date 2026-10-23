# Program: Bar Chart In Spreadsheet
# Question: Write a program to create bar chart using above spreadsheet in Q.19.

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
ws = wb.active
ws.title = "Admissions"
for row in [["Year", "admitted students"], [2022, 700], [2023, 720], [2024, 735], [2025, 840]]:
    ws.append(row)

chart = BarChart()
data = Reference(ws, min_col=2, min_row=1, max_row=5)         # values (with header as title)
categories = Reference(ws, min_col=1, min_row=2, max_row=5)   # years
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, "D2")
wb.save("bar_chart.xlsx")
print("bar_chart.xlsx created")
