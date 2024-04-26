import soundcard as sc
from whisper_mic.whisper_mic import WhisperMic

# デフォルトのマイクを選択
default_mic = sc.default_microphone()

mic = WhisperMic(model='base', verbose=True, save_file=True, input_device=default_mic)
mic.listen_loop()