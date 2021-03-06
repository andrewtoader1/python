import numpy as np
import sounddevice as sd
import time

'''
	@Author: Andrew Toader
	@Date: 15 May 2020
	@Purpose: Class to create a sine wave to play through speakers. For use in synthesizer application.
'''

# Define a sine class to create a sin waveform to play with specified frequency and duration
class Sin:
	# Constructor
	def __init__(self, frequency, duration, attenuate=None):
		# Set member elements of Sine class
		self.frequency = frequency
		self.duration = duration

		# Set the sample frequency to 44.1 kHz
		self.sample_freq = 44100

		# Create time and wave vector
		self.t = np.arange(0, duration, 1/self.sample_freq)			# Period = 1/Frequency
		self.x = np.sin(2 * np.pi * self.frequency * self.t)		# 2*pi*f to convert to angular frequency omega

		# If user wants to attenuate the signal, attenuate by that value (must be less than 1)
		if((attenuate != None) & (attenuate < 1)):
			self.x = self.x * attenuate

	# Member function to play the sine wave through speakers
	def play(self):
		sd.play(self.x, self.sample_freq)
		time.sleep(self.duration)