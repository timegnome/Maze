import os, sys
import pytesseract
from datetime import datetime
try:
    from PIL import Image
except ImportError:
    import Image
# import random
# random.seed(datetime.ctime)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
locpath = "FlaskApp/static/assets/images/location/"
textpath = "FlaskApp/static/assets/images/text/"
print(pytesseract.pytesseract.tesseract_cmd)
images = os.listdir( locpath )
textimg = os.listdir( textpath )
text = []
# print(textimg)
# print(images)

for img in textimg:
    try:
        print(textpath+img)
#         im = Image.open(textpath+img)  
#         # This method will show image in any image viewer  
#         im.show()  
        text.append(pytesseract.image_to_string(Image.open(textpath+img), timeout = 4))
    except RuntimeError as timeout_error:
        print(textpath+img,'fail')
        pass
#     break
print(text)