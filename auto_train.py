import pyautogui
import time
pyautogui.FAILSAFE = True
# 画面の解像度を取得
screenWidth, screenHeight = pyautogui.size()
print(screenWidth)
print(screenHeight)
# マウスを画面中央に移動
pyautogui.moveTo(screenWidth / 2, screenHeight / 2, 2)

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
