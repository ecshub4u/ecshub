# Q19. Create spreadsheet with Year and admitted students (From Professor's Notes)
from openpyxl import Workbook

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

wb.save("admission.xlsx")
print("Admission spreadsheet created successfully")
