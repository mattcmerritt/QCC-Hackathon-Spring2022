from PIL import Image
import pyautogui
import time

print("The screenshot will be taken in 5 seconds, get ready!")
time.sleep(5)
image = pyautogui.screenshot()
print("Screenshot taken!")

# If you want to save the image, uncomment this
# image.save("screenshot.png", "PNG")