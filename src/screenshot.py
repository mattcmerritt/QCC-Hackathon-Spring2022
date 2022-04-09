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
    image.save("screenshot.png", "PNG")

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

    original = Image.open("screenshot.png")
    small = original.resize((int(original.width/2), int(original.height/2)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(small)

    window = Toplevel()

    window.title('Screenshot')
    window.geometry(str(int(original.width/2)) + "x" + str(int(original.height/2)) + "+10+20")
    window.bind('<Button-1>', lambda onclick : set_top_left(window))
    window.bind('<ButtonRelease-1>', lambda onclick : set_bottom_right_and_crop(window, small))

    img_label = Label(window, image=img)
    img_label.pack()

    window.mainloop()

def set_top_left(window):
    global topleft 
    topleft = (window.winfo_pointerx(), window.winfo_pointery())
    print("down")

def set_bottom_right_and_crop(window, image):
    global bottomright 
    bottomright = (window.winfo_pointerx(), window.winfo_pointery())
    image.crop((topleft[0], topleft[1], bottomright[0], bottomright[1])).save("cropped.png", "PNG")
    print("up")



create_window()