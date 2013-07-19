import pyaudio
import numpy as np
import wave
import struct

'''

def getFrequency():
	length = int(LENGTH*RATE)
	##used this equation from modulator to find factor: sineWave = numpy.sin(numpy.arange(length)*factor)
	factor = arcsin(sineWave)/numpy.arange(length)
	##used this equation from modulator to find frequency: factor = float(frequency)*(math.pi*2)/RATE
	frequency = float(factor*RATE/(math.pi*2))
	return frequency

def getNibble(frequency):

	aLo = '0000'
	bLo = '0001'
	cLo = '0010'
	dLo = '0011'
	eLo = '0100'
	fLo = '0101'
	gLo = '0110'
	hLo = '0111'
	aHi = '1000'
	bHi = '1001'
	cHi = '1010'
	dHi = '1011'
	eHi = '1100'
	fHi = '1101'
	gHi = '1110'
	hHi = '1111'

	if frequency=400:
		nibble == aLo
	elif frequency=600:
		nibble == bLo
	elif frequency=800:
		nibble == cLo
	elif frequency=1000:
		nibble == dlo
	elif frequency=1200:
		nibble == eLo
	elif frequency=1400:
		nibble == fLo
	elif frequency=1600:
		nibble == gLo
	elif frequency=1800:
		nibble == hLo
	elif frequency=2000:
		nibble == aHi
	elif frequency=2200:
		nibble == bHi
	elif frequency=2400:
		nibble == cHi
	elif frequency=2600:
		nibble == dHi
	elif frequency=2800:
		nibble == eHi
	elif frequency=3000:
		nibble == fHi
	elif frequency=3200:
		nibble == gHi
	elif frequency=3400:
		nibble == hHi

	return nibble

def writeToFile(nibble):
	try:
		postFile = 'demodBinary.txt'
		postFileOpen = open(postFile, 'a')
		postFileOpen.write(nibble)
	except:
		print "Error in convertToBinary function"
	finally:
		return postFileName
		preFileOpen.close()
		postFileOpen.close()

'''

try:
	filename = raw_input('Enter .wav filename to convert > ')
except:
	print "You entered an invalid filename."

p = pyaudio.PyAudio()
wf = wave.open(filename, 'rb')

print 'Framerate: ',wf.getframerate()


CHUNK = 8820 #gotten from create sound method of modulator
FORMAT = p.get_format_from_width(wf.getsampwidth())
CHANNELS = wf.getnchannels()
RATE = wf.getframerate()
LENGTH = 0.2 #gotten from length specified in createSound method of modulator

'''
frequency = getFrequency()
nibble = getNibble(frequency)
outputFile = writeToFile(nibble)
print 'Your file has been written into ', outputFile
'''








'''
##test stuff



wf = wave.open(filename, 'rb')
rate = wf.getframerate()
print wf
wfParams = str(wf.getparams())

#instantiate the pyaudio library
p = pyaudio.PyAudio()

#signal = wf.getparams()
signal = np.array([1, 2, 44100, 1337344], dtype=float)
fourier = np.fft.fft(signal)
n = signal.size
timestep = 0.2
freq = np.fft.fftfreq(n, d=timestep)
print freq
freq_hz = abs(freq*rate)
print freq_hz
'''