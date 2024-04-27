import whisper
import soundcard as sc
import threading
import queue
import numpy as np
import argparse

def whisper_main():
    SAMPLE_RATE = 16000
    INTERVAL = 3
    BUFFER_SIZE = 4096

    parser = argparse.ArgumentParser()
    parser.add_argument('--model', default='small')
    args = parser.parse_args()

    print('モデルをロード中...')
    model = whisper.load_model(args.model)
    print('完了')

    q = queue.Queue()
    b = np.ones(100) / 100

    options = whisper.DecodingOptions(fp16=False)

    def recognize():
        while True:
            audio = q.get()
            if (audio ** 2).max() > 0.001:
                audio = whisper.pad_or_trim(audio)
                mel = whisper.log_mel_spectrogram(audio).to(model.device)
                _, probs = model.detect_language(mel)
                result = whisper.decode(model, mel, options)
                print(f'{max(probs, key=probs.get)}: {result.text}')

    th_recognize = threading.Thread(target=recognize, daemon=True)
    th_recognize.start()

    with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE, channels=1) as mic:
        audio = np.empty(SAMPLE_RATE * INTERVAL + BUFFER_SIZE, dtype=np.float32)
        n = 0
        while True:
            while n < SAMPLE_RATE * INTERVAL:
                data = mic.record(BUFFER_SIZE)
                audio[n:n+len(data)] = data.reshape(-1)
                n += len(data)

            m = n * 4 // 5
            vol = np.convolve(audio[m:n] ** 2, b, 'same')
            m += vol.argmin()
            q.put(audio[:m])

            audio_prev = audio
            audio = np.empty(SAMPLE_RATE * INTERVAL + BUFFER_SIZE, dtype=np.float32)
            audio[:n-m] = audio_prev[m:n]
            n = n-m

if __name__ == "__main__":
    whisper_main()