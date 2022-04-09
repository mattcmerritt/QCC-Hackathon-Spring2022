from gtts import gTTS
import os

currentString = 'Please dear god let this work'

language = 'en'

myTTS = gTTS(text = currentString, lang = language, slow = False)

myTTS.save("currentString.mp3")

os.system("currentString.mp3")