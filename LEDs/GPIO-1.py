"""Created by MrTijn/Tijndagamer
Interaction with the GPIO
"""

import RPi.GPIO as GPIO
import time

# Setup the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup the Button
ButtonPin = 25
GPIO.setup(ButtonPin, GPIO.IN)

# Setup the LED
LEDPin = 18
GPIO.setup(LEDPin, GPIO.OUT)

# Setup the Buzzer
BuzzerPin = 22
GPIO.setup(BuzzerPin, GPIO.OUT)


def LED(NewState): #Turns the LED on or off
	if NewState == "HIGH":
		GPIO.output(LEDPin, GPIO.HIGH)
	elif NewState == "LOW":
		GPIO.output(LEDPin, GPIO.LOW)
	else:
		print("Error, invalid state")


def Buzzer(): #Buzzes for 1 second
	GPIO.output(BuzzerPin, GPIO.HIGH)
	time.sleep(0.001)
	GPIO.output(BuzzerPin, GPIO.LOW)


def ButtonLoop(): #The while loop for the button
	while True:
		try:
			if GPIO.input(ButtonPin) == False:
				LED("HIGH")
				Buzzer()
			else:
				LED("LOW")
		except KeyboardInterrupt:
			GPIO.cleanup()


ButtonLoop()
