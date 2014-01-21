DataModulator
=============

jsr5194

Special thanks to j105rob, jtpecsi, and DylSec for all their help

Prinamry resource: Iftach Ian Amit at http://www.iamit.org/blog/2012/01/advanced-data-exfiltration/


This repository is for a project for a program that will modulate data from a 
file to sound then from sound back to data

In order for this program to run, make sure to have installed the following:

numpy
pyaudio

Also, it requires use of the math and os python libraries which are default
libraries with python. If you do not have these installed for some reason,
make sure to install them first.

NOTE:
an error like the following will appear in the terminal output. This is due
to restrictions on the project task not allowing external programs such as 
jack server.

	ALSA lib pcm_dmix.c:1018:(snd_pcm_dmix_open) unable to open slave
	ALSA lib pcm.c:2217:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
	ALSA lib pcm.c:2217:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
	ALSA lib pcm.c:2217:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
	ALSA lib audio/pcm_bluetooth.c:1614:(audioservice_expect) BT_GET_CAPABILITIES failed : Input/output error(5)
	ALSA lib audio/pcm_bluetooth.c:1614:(audioservice_expect) BT_GET_CAPABILITIES failed : Input/output error(5)
	ALSA lib audio/pcm_bluetooth.c:1614:(audioservice_expect) BT_GET_CAPABILITIES failed : Input/output error(5)
	ALSA lib audio/pcm_bluetooth.c:1614:(audioservice_expect) BT_GET_CAPABILITIES failed : Input/output error(5)
	ALSA lib pcm_dmix.c:957:(snd_pcm_dmix_open) The dmix plugin supports only playback stream
	ALSA lib pcm_dmix.c:1018:(snd_pcm_dmix_open) unable to open slave
	Cannot connect to server socket err = No such file or directory
	Cannot connect to server socket
	jack server is not running or cannot be started



