from gtts import gTTS
from playsound import playsound
import os

currentString = 'Please dear god let this work. This is another sentence, and I have a lot more to say. You had better keep listening or I will be very upset.'

language = 'en'

myTTS = gTTS(text = currentString, lang = language, slow = False)

myTTS.save("currentString.mp3")

path = os.getcwd() + '\\currentString.mp3'
playsound(path)