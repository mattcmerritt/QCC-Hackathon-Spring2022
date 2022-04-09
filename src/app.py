from gtts import gTTS
import os

from PIL import Image
import pytesseract

debug = True

# setting up pytesseract with executable
if (debug):
    dir = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
else:
    dir = input("Please input the path to the Tesseract OCR executable: ")
pytesseract.pytesseract.tesseract_cmd = dir


# code for playing the sound
def readAloud(currentString):
    myTTS = gTTS(text = currentString, lang = 'en', slow = False)

    myTTS.save(r"files\currentString.mp3")

    os.system(r"files\currentString.mp3")

def readImage(imgPath):
    return pytesseract.image_to_string(Image.open(imgPath))

# print(readImage(r"files\demoImage.png"))
# print(readImage(r"files\demoImage2.png"))
readAloud(readImage(r"files\demoImage.png"))