import text_to_speech as tts

import time
import requests

while True:
    tts.synthesize_speech("こんにちは。")
    time.sleep(5)


