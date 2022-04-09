from gtts import gTTS
from pygame import mixer
import os
import time

import pytesseract

from tkinter import *
from PIL import Image, ImageTk

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
def read_aloud(currentString):
    myTTS = gTTS(text = currentString, lang = 'en', slow = False)

    myTTS.save(r"files\currentString.mp3")

    path = os.getcwd() + r"\files\currentString.mp3"

    mixer.music.load(path)
    mixer.music.play()

# code for reading characters from image to string
def read_image(img_path, is_paragraph=True):
    img_text = pytesseract.image_to_string(Image.open(img_path))

    if is_paragraph:
        # removing newline characters for better reading sound
        img_text = img_text.replace('\n', '')

    return img_text

def create_window():
    window = Tk()

    pause_button = Button(window, text = "Pause")

    pause_button.place(x = 100, y = 60)

    pause_raw = Image.open(os.getcwd() + r"\images\pause.png")
    play_raw = Image.open(os.getcwd() + r"\images\play.png")

    pause_resized = pause_raw.resize((100, 100), Image.ANTIALIAS)
    play_resized = play_raw.resize((100, 100), Image.ANTIALIAS)

    pause_img = ImageTk.PhotoImage(pause_resized)
    play_img = ImageTk.PhotoImage(play_resized)

    # pause_img = PhotoImage(file=os.getcwd() + r"\images\pause.png")
    # play_img = PhotoImage(file=os.getcwd() + r"\images\play.png")

    pause_button.config(image=pause_img)

    pause_button.bind('<Button-1>', lambda onclick : pause(pause_button, pause_img, play_img))

    window.title('Text to Speech Reader')
    window.geometry("300x200+10+20")
    window.mainloop()

def pause(button, pause_img, play_img):
    if (mixer.music.get_busy()):
        mixer.music.pause()
        button.config(image=play_img)
    else:
        mixer.music.unpause()
        button.config(image=pause_img)

read_aloud(read_image(r"files\screenshot.png"))
create_window()
