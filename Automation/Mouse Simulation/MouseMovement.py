from random import uniform
import pyautogui as py
import time

try:
    while True:
        
        py.moveTo(uniform(0, py.size().width), uniform(0, py.size().height), # Screen Size
                  uniform(0.6, 2.7), # Movement speed
                  py.easeOutQuad)
        
        # Sleep Time
        time.sleep(uniform(2, 4))

except KeyboardInterrupt:
    print("Script terminated by user")
