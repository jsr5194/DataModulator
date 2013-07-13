#Main Source: http://www.iamit.org/blog/2012/01/advanced-data-exfiltration/
#Code Help: http://milkandtang.com/blog/2013/02/16/making-noise-in-python/
import math
import numpy
import os
import pyaudio


def convertToBinary(preFileName): #exports to file
	try:
		postFileName = 'binary.txt'
		preFileOpen = open(preFileName, 'rb')
		postFileOpen = open(postFileName, 'w')
		for data in [line.strip() for line in preFileOpen]:
			hexData = data.encode('hex')
			binData = bin(int('1'+hexData, 16))[3:]
			linebreak = '0000110100001010'
			postFileOpen.write(binData+linebreak) #this number is to add in the line break
	except:
		print "you got an error. i'm not smart enough to know which one"
	finally:
		return postFileName
		preFileOpen.close()
		postFileOpen.close()

def playSound(nibble):
	print nibble
	frequency = 0;
	print frequency
	#key	
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
	
	if nibble == aLo:
		frequency=400
	elif nibble == bLo:
		frequency=600
	elif nibble == cLo:
		frequency=800
	elif nibble == dLo:
		frequency=1000
	elif nibble == eLo:
		frequency=1200
	elif nibble == fLo:
		frequency=1400
	elif nibble == gLo:
		frequency=1600
	elif nibble == hLo:
		frequency=1800
	elif nibble == aHi:
		frequency=2000
	elif nibble == bHi:
		frequency=2200
	elif nibble == cHi:
		frequency=2400
	elif nibble == dHi:
		frequency=2600
	elif nibble == eHi:
		frequency=2800
	elif nibble == fHi:
		frequency=3000
	elif nibble == gHi:
		frequency=3200
	elif nibble == hHi:
		frequency=3400

	p = pyaudio.PyAudio()
	sound = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
	createSound(sound, frequency)
	sound.close()
	p.terminate()


#creates the nibble from the earlier created file and sends it into playSound
def createNibble(binFileName):
	try: 
		openBinaryTxt = open(binFileName, 'r')
		readBinaryTxt = ' '
		nibbleArray = []
		while readBinaryTxt != '':
			readBinaryTxt = openBinaryTxt.read(1)
			if len(nibbleArray) == 4:
				nibble = ''.join(nibbleArray)
				playSound(nibble)
				del nibbleArray[:]
				nibbleArray.append(readBinaryTxt)
			else:
				nibbleArray.append(readBinaryTxt)
	except:
		pass		
		

#method to create the sine wave
def createSineWave(frequency, length, rate):
	length = int(length * rate)
	factor = float(frequency)*(math.pi*2)/rate 
	sineWave = numpy.sin(numpy.arange(length)*factor) #this uses numpy to create the sine wave
	return sineWave 

#method to actually play the sound: length = how long it plays, rate=sample rate of device
def createSound(sound, frequency, length=.2, rate=44100): 
	chunks = []
	chunks.append(createSineWave(frequency, length, rate))
	chunk = numpy.concatenate(chunks) * 0.25
	sound.write(chunk.astype(numpy.float32).tostring()) #adds the chunks to the sound variable in 32bit format
	
binFileCheck = os.system("ls | grep 'binary.txt'")
if binFileCheck == 0:
	print "Removing previous binary.txt file"
	os.system('rm binary.txt')

try: 
	fileName = raw_input('Enter Filename To Convert: ')
except:
	print 'Invalid filename'
#fileName = 'picture.png'
#writes the binary output to a file and returns filename
binaryFileName = convertToBinary(fileName) 

createNibble(binaryFileName)
