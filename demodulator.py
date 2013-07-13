import pyaudio
import wave
import time


CHUNK = 1024
filename = raw_input('Enter Filename of .wav file to use > ')

wf = wave.open(filename, 'rb')
print wf
#instantiate the pyaudio library
p = pyaudio.PyAudio()

#create the stream from the given file
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
		channels = wf.getnchannels(),
		rate = wf.getframerate(),
		output = True)

#read the data from the stream
data = wf.readframes(CHUNK)
print wf.getparams()

#play the stream
while data != '':
	stream.write(data)
	data = wf.readframes(CHUNK)

#stop the stream
stream.stop_stream()
stream.close()
wf.close()

#stop pyaudio
p.terminate()
