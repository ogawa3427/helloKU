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

emotes = {
    "happy": [0,0],
    "sad": [0,0],
    "angry": [0,0],
    "surprised": [0,0]
}

def expr_emote(name):
    if not name in emotes:
        print("emote not found")
        return
    pyautogui.click(0, 0)
    time.sleep(random.uniform(0.2, 0.5))
    pyautogui.click(emotes[name][0], emotes[name][1])
    time.sleep(random.uniform(0.2, 0.5))




