import pyaudio
import wave
import time

FRAME = 1
CHUNK = 8820
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
WAVE_OUTPUT_FILENAME = "output.wav"
offsetCheck = True

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=FRAME)

print("* recording")


frames = []
framesDisplay = []
framesTemp = []



try:
	while stream.is_active():
		if offsetCheck == True:
			offsetFrame = 1
			offsetCheck = False
		elif offsetCheck == False:
			offsetFrame += CHUNK
		data = stream.read(FRAME)
		frames.append(data)
		hexData = data.encode('hex')
		binData = bin(int('1'+hexData, 16))[3:]
	   	framesTemp.append(binData)
	   	framesDisplay.append(framesTemp[0])
		del framesTemp[:]
except KeyboardInterrupt:
	print("* done recording")
	#print 'First frame: \t',frames[0], '\nSecond frame: \t', frames[1], '\nThird frame: \t',frames[2], '\nFourth frame: \t', frames[3]
	for count in range (0, 10):
		print 'Frame',count,' : ',framesDisplay[count]
	


stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()