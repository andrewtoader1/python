from sin import *
from square import *
from saw import *

'''
	@Author: Andrew Toader
	@Date: 15 May 2020
	@Purpose: Class to create a scale from a specified start note using the sine wave, square wave, and the sawtooth wave
			  To be used to play different notes of the major scale in the synthsizier applicaiton
'''

# Create dictionary to translate from keyboard input to index in waveform vector in Scale class
# First index is type of waveform (0 = Sine, 1 = Square, 2 = Saw)
# Second index is the index of the note in the scale
note_ind = { ord('a') : [0, 0],
			 ord('s') : [0, 1],
			 ord('d') : [0, 2],
			 ord('f') : [0, 3],
			 ord('g') : [0, 4],
			 ord('h') : [0, 5],
			 ord('j') : [0, 6],
			 ord('k') : [0, 7],
			 ord('q') : [1, 0],
			 ord('w') : [1, 1],
			 ord('e') : [1, 2],
			 ord('r') : [1, 3],
			 ord('t') : [1, 4],
			 ord('y') : [1, 5],
			 ord('u') : [1, 6],
			 ord('i') : [1, 7],
			 ord('z') : [2, 0],
			 ord('x') : [2, 1],
			 ord('c') : [2, 2],
			 ord('v') : [2, 3],
			 ord('b') : [2, 4],
			 ord('n') : [2, 5],
			 ord('m') : [2, 6],
			 ord(',') : [2, 7]
			}


# Class which creates a vector of waveform classes that represent C major scale
class Scale:

	def __init__(self, duration, attenuation=None):
		# Set member variables
		self.duration = duration

		if((attenuation != None) & (attenuation < 1)):		# Attenuation must be a number less than 1
			self.attenuation = attenuation

		# Create a list of waveforms that represent the pitches [C, D, E, F, G, A, B, C]
		self.sin_wv = [Sin(262.0, duration, attenuation), Sin(294.8, duration, attenuation), Sin(327.5, duration, attenuation), Sin(349.3, duration, attenuation), Sin(393.0, duration, attenuation), Sin(436.7, duration, attenuation), Sin(491.2, duration, attenuation), Sin(524.0, duration, attenuation)]
		self.square_wv = [Square(262.0, duration, attenuation), Square(294.8, duration, attenuation), Square(327.5, duration, attenuation), Square(349.3, duration, attenuation), Square(393.0, duration, attenuation), Square(436.7, duration, attenuation), Square(491.2, duration, attenuation), Square(524.0, duration, attenuation)]
		self.saw_wv = [Saw(262.0, duration, attenuation), Saw(294.8, duration, attenuation), Saw(327.5, duration, attenuation), Saw(349.3, duration, attenuation), Saw(393.0, duration, attenuation), Saw(436.7, duration, attenuation), Saw(491.2, duration, attenuation), Saw(524.0, duration, attenuation)]

	def playNote(self, wave_type, note_index):
		if(wave_type == 0):
			self.sin_wv[note_index].play()
		elif(wave_type == 1):
			self.square_wv[note_index].play()
		else:
			self.saw_wv[note_index].play()