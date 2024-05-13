import pyautogui
import time
import hashlib


from datetime import datetime

import sys
args = sys.argv
# 現在の日時を取得
current_time = datetime.now()


# 分と秒を取得
current_minute = current_time.minute
current_second = current_time.second


# 分と秒を表示
print(f"現在の分: {current_minute}")
print(f"現在の秒: {current_second}")


to_hash = str(current_minute) + str(current_second)
print(to_hash)
# ハッシュ値を生成
hash_value = hashlib.md5(to_hash.encode()).hexdigest()
print(hash_value)


#ハッシュ値を１文字ずつのリストに変換
hash_list = list(hash_value)
#各値を整数に変換
hash_list = [int(x, 16) for x in hash_list]
print(hash_list)


class CyclicValueReader:
    def __init__(self, values):
        self.values = values
        self.index = 0


    def get_next_value(self):
        value = self.values[self.index]
        self.index = (self.index + 1) % len(self.values)
        return value/100


# リストの内容を順繰りに返すインスタンスを作成
cyclic_reader = CyclicValueReader(hash_list)


def mouse_position():
    print("マウス")
    print(pyautogui.position())


def my_click(position_x, position_y):
    time.sleep(cyclic_reader.get_next_value()*10)
    pyautogui.moveTo(position_x, position_y, duration=cyclic_reader.get_next_value()*10)
    time.sleep(cyclic_reader.get_next_value()*10)
    pyautogui.click()
    time.sleep(cyclic_reader.get_next_value()*10)

def open_menu():
    time.sleep(cyclic_reader.get_next_value()*10)
    my_click(35, 78)


pyautogui.FAILSAFE = False

if False:
    pyautogui.moveTo(40, 919, duration=cyclic_reader.get_next_value())
    mouse_position()
    pyautogui.click(40, 919)


    print("OpenComment")
    time.sleep(cyclic_reader.get_next_value())
    time.sleep(1)
    pyautogui.click(125, 907)
    time.sleep(1)
    time.sleep(cyclic_reader.get_next_value())
    pyautogui.write("Hello", interval=cyclic_reader.get_next_value())
    print("WriteComment")
    time.sleep(cyclic_reader.get_next_value())
    pyautogui.press('enter')
    print("EnterComment")


    pyautogui.moveTo(546, 988, duration=cyclic_reader.get_next_value()*10)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.mouseDown(895,540, duration=cyclic_reader.get_next_value()*10)
    pyautogui.click()


    print("Shoot!")


    pyautogui.moveTo(470, 676, duration=cyclic_reader.get_next_value()*10)
    pyautogui.click()

    time.sleep(1)

    my_click(912, 67)
    time.sleep(cyclic_reader.get_next_value()*10)
    pyautogui.press('esc')

    my_click(32, 916)
if args[1] != "no":
    open_menu()
    my_click(636, 941)
    my_click(654, 101)
    my_click(758, 627)
    for i in range(10):
        time.sleep(1)
        print(i)
    open_menu()
    my_click(877, 934)
    time.sleep(2)
    my_click(375, 534)

    time.sleep(cyclic_reader.get_next_value()*10)
    my_click(917, 57)
    time.sleep(cyclic_reader.get_next_value()*10)
    my_click(451, 801)

open_menu()
my_click(879, 936)
time.sleep(2)
my_click(375, 534)

time.sleep(cyclic_reader.get_next_value()*10)
my_click(917, 57)
time.sleep(cyclic_reader.get_next_value()*10)
my_click(451, 801)

print("Stored")

my_click(178, 435)
time.sleep(1)
my_click(825, 896)
for i in range(3):
    time.sleep(1)
    print(i)
my_click(889, 175)
time.sleep(cyclic_reader.get_next_value()*10)
my_click(79, 47)
time.sleep(cyclic_reader.get_next_value()*10)
my_click(467, 56)
time.sleep(cyclic_reader.get_next_value()*10)
for i in range(3):
    time.sleep(1)
    print(i)
my_click(77, 47)
time.sleep(cyclic_reader.get_next_value()*10)
my_click(813, 927)
time.sleep(cyclic_reader.get_next_value()*10)
my_click(582, 937)
time.sleep(cyclic_reader.get_next_value()*10)
my_click(19, 52)
time.sleep(cyclic_reader.get_next_value()*10)
my_click(19, 52)

exit()


pyautogui.keyDown('z')
time.sleep(2)
pyautogui.keyUp('z')
print("Scroll")
pyautogui.vscroll(10)


pyautogui.dragTo(100, 100, duration=cyclic_reader.get_next_value()*100)


print("Finish")


mouse_position()
pyautogui.moveTo(100, 100, duration=1)
mouse_position()
# 画面の解像度を取得
screenWidth, screenHeight = pyautogui.size()
print(screenWidth)
print(screenHeight)
mouse_position()
# マウスを画面中央に移動
pyautogui.moveTo(screenWidth / 2, screenHeight / 2, 2)
mouse_position()


# マウスを左クリック
pyautogui.click()


# キーボードで "Hello, world!" と入力
pyautogui.write('Hello, world!', interval=0.25)


# スクリーンショットを取り、ファイルに保存
#screenshot = pyautogui.screenshot()
#screenshot.save('screenshot.png')


import pyautogui
import time
from PIL import Image, ImageDraw


pyautogui.FAILSAFE = True
screenWidth, screenHeight = pyautogui.size()
print(screenWidth)
print(screenHeight)
pyautogui.moveTo(screenWidth / 2, screenHeight / 2, 2)
pyautogui.click()
pyautogui.write('Hello, world!', interval=0.25)


# マウスの位置に基づいて画像を生成し表示するループ
while True:
    x, y = pyautogui.position()
    img = Image.new('RGB', (100, 100), color = (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.ellipse((40, 40, 60, 60), fill=(255, 0, 0))
    img.show()
    time.sleep(1)  # 1秒ごとに画像を更新
# マウスを画面の左上に移動
pyautogui.moveTo(0, 0, 2)



