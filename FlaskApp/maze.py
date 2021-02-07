
from flask import Flask, render_template, request, redirect
from FlaskApp import app
# from os import environ
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

images = os.listdir( locpath )
textimg = os.listdir( textpath )
text = []
# print(textimg)
# print(images)
# Convert the images of text for each page to text and stored into an array for data reference later.
for img in textimg:
    try:
        text.append(pytesseract.image_to_string(Image.open(textpath+img), timeout = 2.5))
    except RuntimeError as timeout_error:
        pass


@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/directions')
@app.route('/start')
def home():
    return render_template (
        'start.html'
    )

# Request route for each new page and the beginning page of the books.
@app.route('/maze')
@app.route('/maze-<room>')
def maze(room=0):
    # print(room)
    # print(text[int(room)])
    return render_template (
        'maze.html',
        year = datetime.now().year,
        # image = room,
        data = {'texts' : text[int(room)],
        'rooms' : str(room)}
    )