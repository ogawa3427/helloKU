#https://tadaoyamaoka.hatenablog.com/entry/2022/10/15/175722
import whisper
import soundcard as sc
import threading
import queue
import numpy as np
import argparse

SAMPLE_RATE = 16000
INTERVAL = 3
BUFFER_SIZE = 4096

parser = argparse.ArgumentParser()
parser.add_argument('--model', default='base')
args = parser.parse_args()

print('Loading model...')
model = whisper.load_model(args.model)
print('Done')

q = queue.Queue()
b = np.ones(100) / 100

print('Decoding options')

options = whisper.DecodingOptions()

print('Starting recognition thread')

def recognize():
    while True:
        audio = q.get()
        print(f'Received audio with max amplitude: {(audio ** 2).max()}')  # デバッグ: オーディオの最大振幅を表示
        if (audio ** 2).max() > 0.001:
            audio = whisper.pad_or_trim(audio)
            print(f'Audio after padding/trimming: {audio.shape}')  # デバッグ: パディング/トリミング後のオーディオ形状を表示

            # make log-Mel spectrogram and move to the same device as the model
            mel = whisper.log_mel_spectrogram(audio).to(model.device)
            print(f'Log-Mel spectrogram shape: {mel.shape}')  # デバッグ: ログメルスペクトログラムの形状を表示

            # detect the spoken language
            _, probs = model.detect_language(mel)
            print(f'Detected language probabilities: {probs}')  # デバッグ: 検出された言語の確率を表示

            # decode the audio
            result = whisper.decode(model, mel, options)
            print(f'Decoded text: {result.text}')  # デバッグ: デコードされたテキストを表示

            # print the recognized text
            print(f'{max(probs, key=probs.get)}: {result.text}')


print('Starting recognition thread')

th_recognize = threading.Thread(target=recognize, daemon=True)
th_recognize.start()

print('Starting recording loop')

# start recording
with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE, channels=1) as mic:
    audio = np.empty(SAMPLE_RATE * INTERVAL + BUFFER_SIZE, dtype=np.float32)
    n = 0
    print('Recording audio...')  # デバッグ: オーディオの録音を開始
    while True:
        while n < SAMPLE_RATE * INTERVAL:
            data = mic.record(BUFFER_SIZE)
            print(f'Recorded data shape: {data.shape}')  # デバッグ: 録音されたデータの形状を表示
            audio[n:n+len(data)] = data.reshape(-1)
            n += len(data)

        # find silent periods
        m = n * 4 // 5
        vol = np.convolve(audio[m:n] ** 2, b, 'same')
        m += vol.argmin()
        print(f'Silent period start index: {m}')  # デバッグ: 静かな期間の開始インデックスを表示
        q.put(audio[:m])

        audio_prev = audio
        audio = np.empty(SAMPLE_RATE * INTERVAL + BUFFER_SIZE, dtype=np.float32)
        audio[:n-m] = audio_prev[m:n]
        n = n-m
        print(f'Buffer reset. New buffer length: {len(audio)}')  # デバッグ: バッファリセット後の新しいバッファの長さを表示