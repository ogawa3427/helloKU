from io import BytesIO

import numpy as np
import soundfile as sf
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(sample_rate=16_000) as source:
    print("なにか話してください")
    audio = r.listen(source)

    print("音声処理中 ...")
    wav_bytes = audio.get_wav_data()
    wav_stream = BytesIO(wav_bytes)
    audio_array, sampling_rate = sf.read(wav_stream)
    audio_fp32 = audio_array.astype(np.float32)

    result = model.transcribe(audio_fp32, fp16=False)