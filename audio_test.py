import soundcard as sc
import numpy as np
import tempfile
import os
import wave

# 定数の設定
SAMPLE_RATE = 16000  # サンプルレート
DURATION = 3  # 録音時間（秒）
BUFFER_SIZE = 1024  # バッファサイズ

# デフォルトのマイクとスピーカーを取得
default_mic = sc.default_microphone()
default_speaker = sc.default_speaker()

while True:
    # 一時ファイルの作成
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    file_path = temp_file.name

    # 録音開始
    print("録音を開始します...")
    with default_mic.recorder(samplerate=SAMPLE_RATE) as mic, wave.open(temp_file, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        for _ in range(int(SAMPLE_RATE / BUFFER_SIZE * DURATION)):
            data = mic.record(numframes=BUFFER_SIZE)
            wf.writeframes(data.tobytes())

    # 録音データの再生
    print("録音データを再生します...")
    with wave.open(file_path, 'rb') as wf:
        with default_speaker.player(samplerate=wf.getframerate()) as sp:
            frames = wf.readframes(wf.getnframes())
            sp.play(frames)

    # 一時ファイルの削除
    print("一時ファイルを削除します...")
    os.remove(file_path)

    # ループの終了条件や待機処理をここに追加することができます（例：time.sleep(1)）