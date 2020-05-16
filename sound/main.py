from scale import *
import cv2

'''
	@Author: Andrew Toader
	@Date: 15 May 2020
	@Purpose: Turns computer keyboard into a synthesizer. 8 adjacent keys play the major scale.
			  - Top row of keys (q, w, e, r, t, y, u, i) play the square wave
			  - Middle row of keys (a, s, d, f, g, h, j, k) play the sine wave
			  - Bottom row of keys (z,x,c,v,b,n,m, ',') play the sawtooth wave

	*** DESIGNED FOR macOS, may not work properly on other operating systems ***
'''

# Print out the instructions for the program
print('Instructions:')
print('\t-You must click on image to start playing')
print('\t-Press keys to change the pitch of the synthesizer.')
print('\t-Comes in 3 different waveforms: Sin, Square, and Sawtooth')
print('\t-Upper keys [q, w, e, r, t, y, u, i] are for sawtooth wave')
print('\t-Middle keys [a, s, d, f, g, h, j, k] are for sine wave')
print('\t-Lower keys [z, x, c, v, b, n, m, \',\'] are for square wave')

# Create 3 types of waves with duration 150ms and gain of 0.75
waves = Scale(0.15, 0.75)

# Create cv2 window
cv2.namedWindow("Tone")
cv2.imshow("Tone", cv2.imread('./pics/sin.png'))
cv2.moveWindow("Tone", 0, 0)

# Initialize key variavle
key = None

# Loop until quit using 'p' key to play whatever sounds user wants by pressing keys on keyboard
while(key != ord('p')):

	# If the key pressed is in the dictionary contained in 'scale.py' play the note according to dictionary note_ind
	if(key in note_ind):
		# Display the image of the graph of the correct wave accordingly
		if(note_ind[key][0] == 0):
			cv2.imshow("Tone", cv2.imread('./pics/sin.png'))
		elif(note_ind[key][0] == 1):
			cv2.imshow("Tone", cv2.imread('./pics/square.png'))
		else:
			cv2.imshow("Tone", cv2.imread('./pics/saw.png'))

		# Play the note accordingly
		waves.playNote(note_ind[key][0], note_ind[key][1])

	# Wait for user to enter next note they want to play
	key = cv2.waitKey(0) &0xFF

# Close all windows when the program is done running
cv2.destroyAllWindows()
