# Q22. Create Pie Chart using spreadsheet data from Q19 (From Professor's Notes)
from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference

wb = Workbook()
ws = wb.active

data = [
    ["Year", "admitted students"],
    [2022, 700],
    [2023, 720],
    [2024, 735],
    [2025, 840]
]
for row in data:
    ws.append(row)

# Create a PieChart object
chart = PieChart()

# Define the data for the chart
data_ref = Reference(ws, min_col=2, min_row=1, max_row=5)

# Define the categories (years)
categories = Reference(ws, min_col=1, min_row=2, max_row=5)

# Add data and categories to the chart
chart.add_data(data_ref, titles_from_data=True)
chart.set_categories(categories)

# Add the chart to the worksheet
ws.add_chart(chart, "B7")

wb.save("PieChart_Admission.xlsx")
print("Pie chart created successfully")
