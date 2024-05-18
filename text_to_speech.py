import requests
#import json
import pyaudio
import os
import wave

# 環境変数からVOICEVOXのエンドポイントとスピーカーIDを取得
VOICEVOX_ENDPOINT = "http://localhost:50021"
VOICEVOX_SPEAKER = "2"

def synthesize_speech(text):
    print("🔈音声合成を開始します。")
    print("🔉テキスト: ", text)
    # クエリ作成
    audio_query_response = requests.post(
        f"{VOICEVOX_ENDPOINT}/audio_query?text={text}&speaker={VOICEVOX_SPEAKER}",
        headers={'Content-Type': 'application/json'}
    )
    audio_query_json = audio_query_response.json()
    audio_query_json["speedScale"] = 1.1
    audio_query_json["intonationScale"] = 1.0
    #audio_query_json["pitchScale"] = 0.9

    print("🔉合成reqを送信しました")
    # 音声合成
    synthesis_response = requests.post(
        f"{VOICEVOX_ENDPOINT}/synthesis?speaker={VOICEVOX_SPEAKER}",
        json=audio_query_json,
        headers={"accept": "audio/wav", 'Content-Type': 'application/json'}
    )

    # 音声ファイルとして保存
    with open("output.wav", "wb") as f:
        f.write(synthesis_response.content)
    print("🔊音声ファイルを保存しました。")

    # pyaudioを使用して音声再生
    CHUNK = 1024
    wf = wave.open("output.wav", 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)
    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()

    print("🔇音声再生が終了しました")

    os.remove("output.wav")  # 音声ファイルを削除

# 使用例
#synthesize_speech("環境変数からVOICEVOXのエンドポイントとスピーカーIDを取得")

def tester(text, speaker):
    # クエリ作成
    audio_query_response = requests.post(
        f"{VOICEVOX_ENDPOINT}/audio_query?text={text}&speaker={speaker}",
        headers={'Content-Type': 'application/json'}
    )
    audio_query_json = audio_query_response.json()
    audio_query_json["speedScale"] = 1.1
    #audio_query_json["pitchScale"] = 0.9
    audio_query_json["intonationScale"] = 1.7


    # 音声合成
    synthesis_response = requests.post(
        f"{VOICEVOX_ENDPOINT}/synthesis?speaker={speaker}",
        json=audio_query_json,
        headers={"accept": "audio/wav", 'Content-Type': 'application/json'}
    )

    # 音声ファイルとして保存
    with open("output.wav", "wb") as f:
        f.write(synthesis_response.content)

    # pyaudioを使用して音声再生
    CHUNK = 1024
    wf = wave.open("output.wav", 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)
    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()

    print("音声再生が終了しました。")

    os.remove("output.wav")  # 音声ファイルを削除

