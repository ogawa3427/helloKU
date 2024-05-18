import pyaudio
import wave

print("presentation.py loaded")

def play_sound(name):
    # pyaudioを使用して音声再生
    CHUNK = 1024
    wf = wave.open(name, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)
    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()

    print("playing finished :", name)
    
print("Waiting for the presentation to start...")
print("The next file is 1")

while True:
    input_val = input("Play 1? (y/n): ")
    if input_val == "y":
        break

print("Playing slide 1...")
print("The next file is 2")
play_sound("slide1_voice.wav")

while True:
    input_val = input("Play 2? (y/n): ")
    if input_val == "y":
        break
    
print("Playing slide 2...")
print("The next file is 3")
play_sound("slide2_voice.wav")

while True:
    input_val = input("Play 3? (y/n): ")
    if input_val == "y":
        break
    
print("Playing slide 3...")
print("The next file is 4")
play_sound("slide3_voice.wav")

while True:
    input_val = input("Play 4? (y/n): ")
    if input_val == "y":
        break
    
print("Playing slide 4...")
print("The next file is 5")
play_sound("slide4_voice.wav")

while True:
    input_val = input("Play 5? (y/n): ")
    if input_val == "y":
        break
    
print("Playing slide 5...")
print("The next file is 6")
play_sound("slide5_voice.wav")

while True:
    input_val = input("Play 6? (y/n): ")
    if input_val == "y":
        break
    
print("Playing slide 6...")
print("The next file is 7")
play_sound("slide6_voice.wav")

while True:
    input_val = input("Play 7? (y/n): ")
    if input_val == "y":
        break
    
print("Playing slide 7...")
print("This is the ending of the presentation")
play_sound("slide7_voice.wav")

print("Presentation finished")
print("Exiting...")
exit()