import pyautogui
import time
import random

def write_comment(comment):
    pyautogui.click(34, 916)
    time.sleep(random.uniform(0.2, 0.5))
    pyautogui.write(comment, interval=0.05)
    pyautogui.press("enter")
    time.sleep(random.uniform(0.2, 0.5))
    print("wrote👍", comment)




