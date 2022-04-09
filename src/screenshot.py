from contextlib import nullcontext
from tkinter import *
from PIL import Image, ImageTk
from threading import Thread
import pyautogui
import time
    
topleft = None
bottomright = None

def screenshot(label):
    time.sleep(5)
    image = pyautogui.screenshot()
    label["text"] = "Screenshot taken!"

    # If you want to save the image, uncomment this
    image.save(r"files\screenshot.png", "PNG")

    create_image_window()

def create_window():
    window = Tk()

    screenshot_button = Button(window, text = "Take a screenshot", bg = 'lightblue')
    action_label = Label(window, text="On click, you will have 5 seconds to prepare for the screenshot.")

    screenshot_button.place(anchor='center', x = 200, y = 40)
    action_label.place(anchor='center', x = 200, y = 80)
    screenshot_button.bind('<Button-1>', lambda onclick : screenshot(action_label))

    window.title('Text Grabber')
    window.geometry("400x100+10+20")
    window.mainloop()

def create_image_window():

    original = Image.open(r"files\screenshot.png")
    small = original.resize((int(original.width/2), int(original.height/2)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(small)

    window = Toplevel()

    window.title('Screenshot')
    window.geometry(str(int(original.width/2)) + "x" + str(int(original.height/2)) + "+10+20")

    def set_top_left(event):
        global topleft 
        topleft = (event.x, event.y)

    def set_bottom_right_and_crop(event):
        global bottomright 
        bottomright = (event.x, event.y)
        small.crop((topleft[0], topleft[1], bottomright[0], bottomright[1])).save(r"files\cropped.png", "PNG")

    window.bind('<Button-1>', set_top_left)
    window.bind('<ButtonRelease-1>', set_bottom_right_and_crop)

    img_label = Label(window, image=img)
    img_label.pack()

    window.mainloop()



create_window()