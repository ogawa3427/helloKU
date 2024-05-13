import pyautogui
import time
import hashlib

from datetime import datetime

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

pyautogui.FAILSAFE = False

pyautogui.moveTo(40, 919, duration=cyclic_reader.get_next_value())
mouse_position()
pyautogui.click(40, 919)

pyautogui.press('z', interval=cyclic_reader.get_next_value())

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
