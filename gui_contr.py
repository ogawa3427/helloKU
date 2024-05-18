import pyautogui
import time
import random
import pyperclip

comment_pos = [31, 915]
coment_box_pos = [122, 906]

def write_comment(comment):
    time.sleep(random.uniform(0.2, 0.5))
    pyautogui.click(comment_pos[0], comment_pos[1])
    time.sleep(random.uniform(0.2, 0.5))
    pyautogui.click(coment_box_pos[0], coment_box_pos[1])
    time.sleep(random.uniform(0.2, 0.5))
    pyperclip.copy(comment)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(random.uniform(0.2, 0.5))
    pyautogui.press("enter")
    time.sleep(random.uniform(0.2, 0.5))
    print("wrote👍", comment)
    pyautogui.click(comment_pos[0], comment_pos[1])

emote_pos = [611, 989]


emotes = {
    "qestion": [771, 641],
    "good": [872, 347],
    "bad": [837, 734],
    "exc": [774, 443]
}

def expr_emote(name):
    if not name in emotes:
        print("emote not found")
        return
    # time.sleep(random.uniform(0.5, 0.7))
    # pyautogui.click(emote_pos[0], emote_pos[1])
    # time.sleep(random.uniform(0.5, 0.7))
    # pyautogui.click(emotes[name][0], emotes[name][1])
    # time.sleep(random.uniform(0.5, 0.7)+2.0)
    # pyautogui.click(emote_pos[0], emote_pos[1])
    # print("emoted🤺", name)
    time.sleep(random.uniform(0.5, 0.7))

def emote_question():
    pyautogui.locateOnScreen('question.png')#, confidence=0.7)
    
def find_pixel_color(target_color="#1371F7"):
    screen = pyautogui.screenshot()
    width, height = screen.size

    for x in range(width):
        for y in range(height):
            if screen.getpixel((x, y)) == pyautogui.hexToRGB(target_color):
                print(f"Found target color at: ({x}, {y})")
                return (x, y)
    print("Target color not found")
    return None

emote_question()
