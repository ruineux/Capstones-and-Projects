from random import uniform
import pyautogui as py
import time

while True:
    
    time.sleep(3)  # Wait for 5 seconds
    # Move mouse to (720, 360) with a random duration between 0.6 and 2.7 seconds
    py.moveTo(720, 360, uniform(0.6, 2.7), py.easeOutQuad)
    
    time.sleep(2)  # Wait for 5 seconds
    # Move mouse to (450, 900) with a random duration between 0.6 and 2.7 seconds
    py.moveTo(450, 900, uniform(0.6, 2.7), py.easeOutBack)
    
    time.sleep(3)  # Wait for 5 seconds
    # Move mouse to (360, 720) with a random duration between 0.6 and 2.7 seconds
    py.moveTo(360, 720, uniform(0.6, 2.7), py.easeInOutQuad)