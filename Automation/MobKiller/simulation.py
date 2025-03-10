import pyautogui
from PIL import Image, ImageDraw

import time
import pydirectinput
from directinput import PressKey, ReleaseKey


# Introduce a 2-second delay
time.sleep(2)

# Path to the image file you want to find
image_path = 'D:\Capstones-and-Projects\Automation\MobKiller\HPMPBar.jpg'

adjustment_left = 20
adjustment_top = 100
adjustment_width = 55

# Locate the image on the screen with a confidence level of 0.8 (80%)
location = pyautogui.locateOnScreen(image_path, confidence=0.8)

while pyautogui.locateOnScreen(image_path, confidence=0.8):
    print(f'Image found at: {location}')

    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to a PIL image
    img = Image.new('RGB', screenshot.size, (0, 0, 0))
    img.paste(screenshot)

    # Calculate the center of the found image
    center_x = location.left + location.width // 2
    center_y = location.top + location.height // 2



    # Draw a red rectangle around the found image
    draw = ImageDraw.Draw(img)
    red_box_top_left = (location.left-adjustment_left, location.top-adjustment_top)
    red_box_bottom_right = (location.left + location.width + adjustment_width, location.top + location.height)
    draw.rectangle([red_box_top_left, red_box_bottom_right], outline="red", width=3)

    

    # Draw a larger green rectangle around the red box
    green_box_padding = 5  # Define the padding around the red box
    green_box_top_left = (red_box_top_left[0] - green_box_padding, red_box_top_left[1] - green_box_padding)
    green_box_bottom_right = (red_box_bottom_right[0] + green_box_padding, red_box_bottom_right[1] + green_box_padding)
    draw.rectangle([green_box_top_left, green_box_bottom_right], outline="green", width=3)

    # Recalibrate Center
    green_box_center_x = (green_box_top_left[0] + green_box_bottom_right[0]) // 2
    green_box_center_y = (green_box_top_left[1] + green_box_bottom_right[1]) // 2

    # Coordinates for each side of the green box
    top = (green_box_center_x, green_box_top_left[1])
    top_left = (green_box_top_left[0], green_box_top_left[1])
    top_right = (green_box_bottom_right[0], green_box_top_left[1])
    
    bottom = (green_box_center_x, green_box_bottom_right[1])
    bottom_left = (green_box_top_left[0], green_box_bottom_right[1])
    bottom_right = (green_box_bottom_right[0], green_box_bottom_right[1])
    
    
    left = (green_box_top_left[0], green_box_center_y)
    right = (green_box_bottom_right[0], green_box_center_y)

    coordinates = [top_left, top, top_right, right, bottom_right, bottom, bottom_left, left]

    # Move the mouse to the center of the green box and click
    #pyautogui.moveTo(x=green_box_center_x, y=green_box_center_y)
    #pydirectinput.moveTo(x=green_box_center_x, y=green_box_center_y)

    
    #pyautogui.click(clicks=2, interval=0.25)

    for coordinate in coordinates:
        PressKey(0x3B) #F1
        ReleaseKey(0x3B)
        time.sleep(0.1)
        #pydirectinput.moveTo(*coordinate)
        pyautogui.click(*coordinate, clicks=2)
        #time.sleep(0.1)
        #pyautogui.click(*coordinate, clicks=2)
        #time.sleep(0.1)
        #pyautogui.click(*coordinate, clicks=2)
        #time.sleep(0.1)
        #pyautogui.click(*coordinate, clicks=2)

        



else:
    print('Image not found on the screen.')