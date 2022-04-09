from gtts import gTTS
from pygame import mixer
import os
import time

from PIL import Image
import pytesseract

debug = True

# setting up pytesseract with executable
if (debug):
    dir = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
else:
    dir = input("Please input the path to the Tesseract OCR executable: ")
pytesseract.pytesseract.tesseract_cmd = dir

# setting up pygame mixer
mixer.init()

# code for playing the sound
def readAloud(currentString):
    myTTS = gTTS(text = currentString, lang = 'en', slow = False)

    myTTS.save(r"files\currentString.mp3")

    path = os.getcwd() + r"\files\currentString.mp3"

    mixer.music.load(path)
    mixer.music.play()

    time.sleep(1)
    mixer.music.pause()
    time.sleep(1)
    mixer.music.unpause()
    time.sleep(1)
    mixer.music.stop()
    time.sleep(1)
    mixer.music.play()

# code for reading characters from image to string
def readImage(imgPath, isParagraph=True):
    imgText = pytesseract.image_to_string(Image.open(imgPath))

    if isParagraph:
        # removing newline characters for better reading sound
        imgText = imgText.replace('\n', '')

    return imgText

# print(readImage(r"files\demoImage.png"))
# print(readImage(r"files\demoImage2.png"))
readAloud(readImage(r"files\demoImage.png"))
