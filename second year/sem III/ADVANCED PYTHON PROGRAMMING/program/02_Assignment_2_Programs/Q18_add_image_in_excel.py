# Q18. Add an image in Excel spreadsheet using Pillow and openpyxl (From Professor's Notes)
from PIL import Image
from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage

# Open an image using Pillow (or create a sample image if not present)
img_pil = Image.open("im.jpg")
# Optional: Resize the image
img_pil = img_pil.resize((200, 150))
img_pil.save("resized_image.jpg")

# Create a new workbook and select the active sheet
wb = Workbook()
ws = wb.active

# Create an openpyxl Image object from the image file
img_excel = ExcelImage("resized_image.jpg")

# Add the image to the specified cell (e.g., 'C5')
ws.add_image(img_excel, 'C5')

# Save the workbook
wb.save("imgxl.xlsx")
