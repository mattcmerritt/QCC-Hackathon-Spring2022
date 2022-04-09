from PIL import Image
from tkinter import *
from threading import Thread
import pyautogui
import time

def set_instructions_for_screenshot(label):
    label["text"] = "The screenshot will be taken in 5 seconds, get ready!"

def screenshot_image(label):
    time.sleep(5)
    image = pyautogui.screenshot()
    label["text"] = "Screenshot taken!"
    # If you want to save the image, uncomment this
    image.save("screenshot.png", "PNG")

def screenshot(label):
    instructions_thread = Thread(target=set_instructions_for_screenshot, args=(label,))
    instructions_thread.start()
    screenshot_thread = Thread(target=screenshot_image, args=(label,))
    screenshot_thread.start()

def create_window():
    window = Tk()

    screenshot_button = Button(window, text = "Take a screenshot", bg = 'lightblue')
    action_label = Label(window, text="")

    screenshot_button.place(x = 100, y = 60)
    action_label.place(x = 100, y = 100)
    screenshot_button.bind('<Button-1>', lambda onclick : screenshot(action_label))

    window.title('Text Grabber')
    window.geometry("300x200+10+20")
    window.mainloop()

create_window()