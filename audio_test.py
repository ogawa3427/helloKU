import soundcard as sc
import numpy as np

# サンプリング設定
samplerate = 48000
frames = 1024

# マイクの設定
default_mic = sc.default_microphone()

def monitor_audio():
    while True:
        data = default_mic.record(frames, samplerate)
        data = data.mean(axis=1)  # ステレオをモノラルに変換
        volume = np.linalg.norm(data)  # ボリュームを計算
        volume_bar = '#' * int(volume * 100)  # ボリュームレベルに基づいたバーを生成
        print(f'\r{volume_bar}', end='')  # リアルタイムで表示更新

if __name__ == '__main__':
    monitor_audio()