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

QUESTION_EMOTE = [771, 656]
def emote_question():
    time.sleep(random.uniform(0.5, 0.7))
    pyautogui.click(QUESTION_EMOTE[0], QUESTION_EMOTE[1])

SORENA_EMOTE = [771, 754]
def emote_sorena():
    time.sleep(random.uniform(0.5, 0.7))
    pyautogui.click(SORENA_EMOTE[0], SORENA_EMOTE[1])
    
UTATANE_EMOTE = [867, 457]
def emote_utatane():
    time.sleep(random.uniform(0.5, 0.7))
    pyautogui.click(UTATANE_EMOTE[0], UTATANE_EMOTE[1])


emote_question()

time.sleep(1)

emote_utatane()

time.sleep(1)

emote_sorena()