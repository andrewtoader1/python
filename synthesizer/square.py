import numpy as np
import sounddevice as sd
import time

'''
	@Author: Andrew Toader
	@Date: 15 May 2020
	@Purpose: Class to create a square wave to play through speakers. For use in synthesizer application.
'''

# Define a square class to create a square waveform to play with specified frequency and duration
class Square:
	# Constructor
	def __init__(self, frequency, duration, attenuate=None):
		# Set member elements of Square class
		self.frequency = frequency
		self.duration = duration

		# Set the sample frequency to 44.1 kHz
		self.sample_freq = 44100

		# Create time and wave vector as sine wave first
		self.t = np.arange(0, duration, 1/self.sample_freq)			# Period = 1/Frequency
		self.x = np.sin(2 * np.pi * self.frequency * self.t)		# 2*pi*f to convert to angular frequency omega

		# Convert sine wave to a square wave by making value either -1 or 1
		for i in range(0, self.x.size):
			if(self.x[i] < 0):
				self.x[i] = -1.0
			if(self.x[i] > 0):
				self.x[i] = 1.0

		# If user wants to attenuate the signal, attenuate by that value (must be less than 1)
		if((attenuate != None) & (attenuate < 1)):
			self.x = self.x * attenuate

	# Member function to play the sine wave through speakers
	def play(self):
		sd.play(self.x, self.sample_freq)
		time.sleep(self.duration)