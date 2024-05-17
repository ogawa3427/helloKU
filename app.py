import text_to_speech as tts
import gui_contr as gc

tts.synthesize_speech("こんにちは。")

from io import BytesIO

import numpy as np
import soundfile as sf

import openai
import json
import os
import time

import requests

prev_text = ""

import pyaudio

def play_audio(file_path):
    # 音声ファイルを読み込む
    data, samplerate = sf.read(file_path)
    
    # PyAudioの設定をステレオと16ビット整数形式に変更
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=samplerate,
                    output=True)
    
    # 音声の再生
    stream.write(data.tobytes())
    
    # ストリームを閉じる
    stream.stop_stream()
    stream.close()
    p.terminate()

#play_audio("1.wav")
import speech_recognition as sr

from openai import OpenAI
aiclient = OpenAI()
openai.api_key = os.getenv('OPENAI_API_KEY')


import whisper
model = whisper.load_model("base")
r = sr.Recognizer()
with sr.Microphone(sample_rate=16_000) as source:
        while True:
            try:
                print("😍😍😍なにか話してください")
                time.sleep(1)
                print("😍😍😍なにか話してください22222")
                audio = r.listen(source, timeout=15)

                print("音声処理中 ...")
                wav_bytes = audio.get_wav_data()
                wav_stream = BytesIO(wav_bytes)
                audio_array, sampling_rate = sf.read(wav_stream)
                audio_fp32 = audio_array.astype(np.float32)

                result = model.transcribe(audio_fp32, fp16=False)
                print("🥺🥺🥺")
                print(result["text"])
                if result["text"] == "":
                    tts.synthesize_speech("もう一度")
                    continue 
                prev_text = result["text"]
                gc.expr_emote("happy")
                prompt = result["text"]
                response = aiclient.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": "あなたは対話形式で会話するキャラクターです。他人行儀な話し方はしないでください。入力は音声認識を経由しているため安定しないことがあります、そのため多少は想像して答えて構いません。また返答は日本語にしてください。"},
                            {"role": "user", "content": prompt}]
                )
                answer = response.choices[0].message.content
                if not any(char in answer for char in "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"):
                    tts.synthesize_speech("もう一度")
                    print(answer)
                    continue
                print("☎️☎️☎️AI")
                print(answer)
                source.MUTE = True
                gc.write_comment(answer)
                tts.synthesize_speech(answer)
                source.MUTE = False
                print("🪮🛡️🛡️🛡️BACK")
                time.sleep(0.2)
            except Exception as e:
                print(f"エラーが発生しました: {e}")
                print("最初からやり直します...")
                continue