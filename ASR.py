from concurrent.futures import thread
from scipy.io import wavfile
import numpy as np
import pyaudio
import wave
from array import array

from Speechrecognition.speechrecognition import predict


### SPEECH RECOGNITION ###
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=16000
CHUNK=1024
FILE_NAME="out.wav"

audio=pyaudio.PyAudio() #instantiate the pyaudio

#recording prerequisites
stream=audio.open(format=FORMAT,channels=CHANNELS, 
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)

#starting recording
frames=[]
import time

print(f"Start talking in...")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GO!")
print("listening...")
time.sleep(1)
while True:
    data=stream.read(CHUNK)
    data_chunk=array('h',data)
    frames.append(data)
    vol=max(data_chunk)
    print(vol)
    if(vol>50):
        continue
    else:
        print("good!")
        break


#end of recording
stream.stop_stream()
stream.close()
audio.terminate()
#writing to file
wavfile=wave.open(FILE_NAME,'wb')
wavfile.setnchannels(CHANNELS)
wavfile.setsampwidth(audio.get_sample_size(FORMAT))
wavfile.setframerate(RATE)
wavfile.writeframes(b''.join(frames))#append frames recorded to file
wavfile.close()

# speechrecognition prediction
print("predicting...")
predict("out.wav")

