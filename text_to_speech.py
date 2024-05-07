import requests
import json
import pygame  # playsoundの代わりにpygameをインポート
import os
import time

# 環境変数からVOICEVOXのエンドポイントとスピーカーIDを取得
VOICEVOX_ENDPOINT = "http://localhost:50021"
VOICEVOX_SPEAKER = "2"

def synthesize_speech(text):
    # クエリ作成
    audio_query_response = requests.post(
        f"{VOICEVOX_ENDPOINT}/audio_query?text={text}&speaker={VOICEVOX_SPEAKER}",
        headers={'Content-Type': 'application/json'}
    )
    audio_query_json = audio_query_response.json()
    audio_query_json["speedScale"] = 1.1

    # 音声合成
    synthesis_response = requests.post(
        f"{VOICEVOX_ENDPOINT}/synthesis?speaker={VOICEVOX_SPEAKER}",
        json=audio_query_json,
        headers={"accept": "audio/wav", 'Content-Type': 'application/json'}
    )

    # 音声ファイルとして保存
    with open("output.wav", "wb") as f:
        f.write(synthesis_response.content)

    # pygameを使用して音声再生
    pygame.mixer.init()
    pygame.mixer.music.load("output.wav")
    pygame.mixer.music.play()
    a = 0
    while pygame.mixer.music.get_busy():  # 再生が終了するまで待機
        time.sleep(0.5)
        print(a)
        a += 1

    os.remove("output.wav")  # 音声ファイルを削除

# 使用例
#synthesize_speech("こんにちは。")