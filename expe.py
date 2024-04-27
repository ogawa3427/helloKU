from io import BytesIO

import numpy as np
import speech_recognition as sr
import soundfile as sf
from whisper.audio import load_audio

r = sr.Recognizer()
with sr.Microphone(sample_rate=16_000) as source:
    print("検証します。話してください")
    audio = r.listen(source)

print("検証開始")
wav_bytes = audio.get_wav_data()
with open("tmp_audio.wav", "wb") as f:
    f.write(wav_bytes)
wav_stream = BytesIO(wav_bytes)
audio_array, sampling_rate = sf.read(wav_stream)
audio_fp32 = audio_array.astype(np.float32)

audio_from_file = load_audio("tmp_audio.wav")

print(audio_fp32.shape, audio_from_file.shape)
np.testing.assert_array_equal(audio_fp32, audio_from_file)