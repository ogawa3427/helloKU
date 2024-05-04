import text_to_speech as tts

tts.synthesize_speech("こんにちは。")

from io import BytesIO

import numpy as np
import soundfile as sf

import openai
import json
import os

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
        print(prev_text)
        print("なにか話してください")
        try:
            # 15秒でタイムアウトするように設定
            audio = r.listen(source, timeout=15, phrase_time_limit=15)
        except sr.WaitTimeoutError:
            print("タイムアウト")
            continue

        print("音声処理中 ...")
        wav_bytes = audio.get_wav_data()
        wav_stream = BytesIO(wav_bytes)
        audio_array, sampling_rate = sf.read(wav_stream)
        audio_fp32 = audio_array.astype(np.float32)

        result = model.transcribe(audio_fp32, fp16=False)
        print(result["text"])
        if result["text"] == "":
            tts.synthesize_speech("もう一度")
            continue 
        prev_text = result["text"]

        prompt = result["text"]
        response = aiclient.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."}, 
                    {"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content
        if not any(char in answer for char in "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"):
            tts.synthesize_speech("もう一度")
            print(answer)
            continue
        print(answer)
        tts.synthesize_speech(answer)
