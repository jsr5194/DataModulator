import pyaudio
import wave
import time


CHUNK = 8820
FORMAT = pyaudio.paFloat32
CHANNELS = 1
LENGTH = 0.2
RATE = 44100
FRAME = LENGTH * RATE
#filename = raw_input('Enter Filename of .wav file to use > ')
filename = 'mod.wav'

wf = wave.open(filename, 'rb')
print wf
#instantiate the pyaudio library
p = pyaudio.PyAudio()

#create the stream from the given file
stream = p.open(format = FORMAT,
		channels = CHANNELS,
		rate =RATE,
		output = True,
		frames_per_buffer=CHUNK)

#read the data from the stream



try:
	#play the stream
	while stream.is_active():
		data = wf.readframes(CHUNK)
		stream.write(data)
	
except KeyboardInterrupt:
	hexData = data[0].encode('hex')
	hexData2 = data[1].encode('hex')
	print 'Test Data: ', hexData, ' : ', hexData2
	




#stop the stream
stream.stop_stream()
stream.close()
wf.close()

#stop pyaudio
p.terminate()
