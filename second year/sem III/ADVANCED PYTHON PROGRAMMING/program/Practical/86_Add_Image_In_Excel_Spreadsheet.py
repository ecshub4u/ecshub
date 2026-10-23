# Program: Add Image In Excel Spreadsheet
# Question: Write python program to add any image in excel spreadsheet.

# pip install openpyxl Pillow
# Keep any image named im.jpg in the same folder as this program
from PIL import Image
from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage

img_pil = Image.open("im.jpg")
img_pil = img_pil.resize((200, 150))
img_pil.save("resized_image.jpg")

wb = Workbook()
ws = wb.active
img_excel = ExcelImage("resized_image.jpg")
ws.add_image(img_excel, "C5")
wb.save("imgxl.xlsx")
print("Image added at C5")
