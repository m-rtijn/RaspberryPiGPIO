"""Created by MrTijn/Tijndagamer
Copyright 2014
"""

import RPi.GPIO as gpio
import os

# Setup the gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# Setup the button
ButtonPin = 18
gpio.setup(ButtonPin, gpio.IN)


def ButtonLoop(): #The loop for the button
	while True:
		try:
			if gpio.input(ButtonPin) == False:
				#os.system("clear")
				print("beep")
						
		except KeyboardInterrupt:
			gpio.cleanup()


ButtonLoop()
