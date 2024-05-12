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


# マウスを画面の左上に移動
pyautogui.moveTo(0, 0, 2)
