import pyaudio
import wave
import whisper
import threading

# Whisperモデルのロード
model = whisper.load_model("medium")

def process_audio(data, model):
    # 音声データをテキストに変換
    result = model.transcribe(data)
    transcription = result["text"]
    # ここで送信ロジックを実装
    print(transcription)

def stream_audio():
    chunk = 1024  # レコードブロックサイズ
    format = pyaudio.paInt16  # 16ビットフォーマット
    channels = 1  # モノラル
    rate = 44100  # サンプルレート

    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("録音開始")

    frames = []

    try:
        while True:
            data = stream.read(chunk)
            frames.append(data)
            if len(frames) * chunk >= rate * 5:  # 5秒ごとに処理
                # 別スレッドで音声処理を実行
                threading.Thread(target=process_audio, args=(b''.join(frames), model)).start()
                frames = []  # フレームをリセット
    except KeyboardInterrupt:
        print("録音終了")

    stream.stop_stream()
    stream.close()
    p.terminate()

stream_audio()