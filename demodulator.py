# Read in a WAV and find the freq's
import os
import sys
import pyaudio
import wave
import numpy as np
import binascii


bufferArray = []
linebreakArray = []


def startup():
	if len(sys.argv) != 2:
		os.system("clear")
		print 
		print "********************************************************"
		print "* Incomplete command.  See examples below for usage:   *"
		print "*                                                      *"           
		print "*                   Standard Use                       *"
		print "*                                                      *"
		print "* From a pre-recorded file:                            *"
		print "* python demodulator.py filename.wav                   *"
		print "*                                                      *"
		print "* From raw recording:                                  *"
		print "* python demodulator.py --record                       *"
		print "********************************************************"  
		print 
		raw_input("Hit Enter To Return")
		quit()

	binFileCheck = os.system("ls | grep 'demodBinary.txt'")
	if binFileCheck == 0:
		print "Do you want to delete previous demodBinary.txt file"
		answer = raw_input("(Enter : Yes, CTRL-C : no) >")
		if answer == 'Yes' or answer == 'yes':
			print "Removing previous demodBinary.txt file"
			os.system("rm demodBinary.txt")
		else:
			quit()

	if sys.argv[1] == '--record':

	else:
		wavFile = sys.argv[1]
		getFrequency(wavFile)


def getFrequency(filename):
	chunk = 8820

	# open up a wave
	wf = wave.open(filename, 'rb')
	swidth = wf.getsampwidth()
	RATE = wf.getframerate()
	# use a Blackman window
	window = np.blackman(chunk)
	# open stream
	p = pyaudio.PyAudio()
	os.system("clear");
	stream = p.open(format =
	                p.get_format_from_width(wf.getsampwidth()),
	                channels = wf.getnchannels(),
	                rate = RATE,
	                output = True)

	# read some data
	data = wf.readframes(chunk)
	# play stream and find the frequency of each chunk
	while len(data) == chunk*swidth:
	    # write data out to the audio stream
	    stream.write(data)
	    # unpack the data and times by the hamming window
	    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
	                                         data))*window
	    # Take the fft and square each value
	    fftData=abs(np.fft.rfft(indata))**2
	    # find the maximum
	    which = fftData[1:].argmax() + 1
	    # use quadratic interpolation around the max
	    if which != len(fftData)-1:
	        y0,y1,y2 = np.log(fftData[which-1:which+2:])
	        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
	        # find the frequency and output it
	        thefreq = round((which+x1)*RATE/chunk)
	       # print "The freq is %f Hz." % (thefreq)
	        getNibble(thefreq)
	    else:
	        thefreq = round(which*RATE/chunk)
	       # print "The freq is %f Hz." % (thefreq)
	        getNibble(thefreq)
	    # read some more data
	    data = wf.readframes(chunk)
	if data:
	    stream.write(data)
	stream.close()
	p.terminate()



def getNibble(frequency):

	nibble = ''

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
		frequency=1600
	elif nibble == bLo:
		frequency=1700
	elif nibble == cLo:
		frequency=1800
	elif nibble == dLo:
		frequency=1900
	elif nibble == eLo:
		frequency=2000
	elif nibble == fLo:
		frequency=2100
	elif nibble == gLo:
		frequency=2200
	elif nibble == hLo:
		frequency=2300
	elif nibble == aHi:
		frequency=2400
	elif nibble == bHi:
		frequency=2500
	elif nibble == cHi:
		frequency=2600
	elif nibble == dHi:
		frequency=2700
	elif nibble == eHi:
		frequency=2800
	elif nibble == fHi:
		frequency=3000
	elif nibble == gHi:
		frequency=3200
	elif nibble == hHi:
		frequency=3400

'''
	if frequency==400.000000:
		nibble = aLo
	elif frequency==600.000000:
		nibble = bLo
	elif frequency==800.000000:
		nibble = cLo
	elif frequency==1000.000000:
		nibble = dLo
	elif frequency==1200.000000:
		nibble = eLo
	elif frequency==1400.000000:
		nibble = fLo
	elif frequency==1600.000000:
		nibble = gLo
	elif frequency==1800.000000:
		nibble = hLo
	elif frequency==2000.000000:
		nibble = aHi
	elif frequency==2200.000000:
		nibble = bHi
	elif frequency==2400.000000:
		nibble = cHi
	elif frequency==2600.000000:
		nibble = dHi
	elif frequency==2800.000000:
		nibble = eHi
	elif frequency==3000.000000:
		nibble = fHi
	elif frequency==3200.000000:
		nibble = gHi
	elif frequency==3400.000000:
		nibble = hHi
'''
	writeToFile(nibble)

def writeToFile(nibble):
	try:
		postFile = 'demodBinary.txt'
		postFileOpen = open(postFile, 'a')
		postFileOpen.write(nibble)
		buffer(nibble)
	except:
		pass
	finally:
		postFileOpen.close()




def buffer(nibble):
	if len(bufferArray) == 0:
		bufferArray.append(nibble)
	elif len(bufferArray) == 1:
		linebreakArray1 = ['0000', '1101']
		linebreakArray2 = ['0000', '1010']
		bufferArray.append(nibble)
		if bufferArray == linebreakArray1 or bufferArray == linebreakArray2:
			print '\n'
		else:
			printLetter(bufferArray)
		del bufferArray[:]

	


def printLetter(charArray):
	letterArray = ''.join(charArray)
	letter = binascii.unhexlify('%x'%int('0b'+letterArray,2))
	sys.stdout.write(letter)
	#print letter





startup()
