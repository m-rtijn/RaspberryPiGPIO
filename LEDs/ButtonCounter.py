import RPi.GPIO as gpio
import time
import os

#Setup the gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

#Setup the button
ButtonPin = 18
gpio.setup(ButtonPin, gpio.IN)

start = 0
stop = 0
currentState = False
oldState = False

def ButtonLoop():
	global start
	global stop
	global currentState
	global oldState
	while True:
		currentState = gpio.input(ButtonPin)
		if currentState == False and oldState == True:
			start = time.time()
		elif currentState == True and oldState == False:
			stop = time.time()
		if ((start != 0) and (stop != 0)):
			print(start - stop)
			print(start)
			print(stop)
			start = 0
			stop = 0
		oldState = currentState
try:
	ButtonLoop()
except KeyboardInterrupt:
	gpio.cleanup()
