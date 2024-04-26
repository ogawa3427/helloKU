import soundcard as sc
import whisper
import threading
import numpy as np

# Whisperモデルのロード
model = whisper.load_model("medium")

def process_audio(data, model):
    # バイトデータをNumPy配列に変換
    data = np.frombuffer(data, dtype=np.int16)
    # 音声データをテキストに変換
    result = model.transcribe(data)
    transcription = result["text"]
    print(transcription)

def stream_audio():
    # デフォルトのマイクを選択
    mic = sc.default_microphone()
    samplerate = 44100  # サンプルレート

    with mic.recorder(samplerate, channels=1) as mic_recorder:
        print("録音開始")
        frames = []

        try:
            while True:
                # 1秒間の音声データを取得
                data = mic_recorder.record(samplerate)
                frames.append(data)
                if len(frames) * samplerate >= samplerate * 5:  # 5秒ごとに処理
                    # 別スレッドで音声処理を実行
                    threading.Thread(target=process_audio, args=(b''.join(frames), model)).start()
                    frames = []  # フレームをリセット
        except KeyboardInterrupt:
            print("録音終了")

stream_audio()