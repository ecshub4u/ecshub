# 1. Reading CSV into a dictionary using csv.DictReader() (From Professor's Notes)
import csv
from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill, Border, Side

# 2. Excel Formulas, PatternFill, Border, Number Format (From Professor's Notes)
wb = Workbook()
ws = wb.active

# Formula example from notes
ws["B5"] = 70
ws["C5"] = 77
ws["D5"] = 90
ws["E5"] = "=SUM(B5,C5,D5)"
ws["F5"] = "=AVERAGE(B5,C5,D5)"

# PatternFill example from notes
ws['B3'].fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")

# Border example from notes
border_thick = Side(style='thick')
border_thin = Side(style='thin')
border_dashed = Side(style='dashed')
border_dotted = Side(style='dotted')
ws['F3'].border = Border(top=border_thick, left=border_thin, right=border_dashed, bottom=border_dotted)

# Number Formatting example from notes
ws['F6'] = 14342345.6779
ws['F6'].number_format = '#,##0.00'

wb.save("formula_styles.xlsx")
print("Formulas and styles saved successfully")
