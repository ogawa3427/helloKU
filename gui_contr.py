import pyautogui
import time
import random

comment_pos = [31, 915]
coment_box_pos = [130, 901]

def write_comment(comment):
    pyautogui.click(comment_pos[0], comment_pos[1])
    time.sleep(random.uniform(0.2, 0.5))
    pyautogui.click(coment_box_pos[0], coment_box_pos[1])
    time.sleep(random.uniform(0.2, 0.5))
    pyautogui.write(comment, interval=0.05)
    time.sleep(random.uniform(0.2, 0.5))
    pyautogui.press("enter")
    time.sleep(random.uniform(0.2, 0.5))
    print("wrote👍", comment)
    pyautogui.click(comment_pos[0], comment_pos[1])

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
    pyautogui.click(0, 0)




