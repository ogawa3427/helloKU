import requests
import pygame
import os

def synthesize_speech(text, speaker_id=1):
    api_url = 'http://localhost:50021'  # VOICEVOXのAPIエンドポイント
    audio_query_url = f"{api_url}/audio_query?text={text}&speaker={speaker_id}"
    synthesis_url = f"{api_url}/synthesis?speaker={speaker_id}?is_kana=true"

    # テキストから音声合成のクエリを生成
    response = requests.post(audio_query_url)
    audio_query = response.json()

    # 音声合成クエリから音声データを生成
    response = requests.post(synthesis_url, json=audio_query)
    audio_data = response.content

    # 音声データをファイルに保存
    with open('output.wav', 'wb') as f:
        f.write(audio_data)

    # 音声データを再生
    pygame.mixer.init()
    pygame.mixer.music.load('output.wav')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)
    os.remove('output.wav')
    print("音声データを再生しました。")    

while True:
    print("🥰合成したい音声を入力してください")
    text = input()
    synthesize_speech(text)