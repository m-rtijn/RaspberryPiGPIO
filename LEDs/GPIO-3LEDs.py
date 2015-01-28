"""This script it made by Tijndagamer. 
Copyright 2014.
"""

# Import the required libraries
import RPi.GPIO as GPIO
import time
import random

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Turn of warnings
GPIO.setwarnings(False)

# Setup the Button
ButtonPin = 25
GPIO.setup(ButtonPin, GPIO.IN)

# Setup the Buzzer
BuzzerPin = 22
GPIO.setup(BuzzerPin, GPIO.OUT)

# Setup the green LED
Green_LEDPin = 18
GPIO.setup(Green_LEDPin, GPIO.OUT)

# Setup the yellow LED
Yellow_LEDPin = 23
GPIO.setup(Yellow_LEDPin, GPIO.OUT)

# Setup the red LED
Red_LEDPin = 24
GPIO.setup(Red_LEDPin, GPIO.OUT)

# Global variables
RandomPin = 18


def LED(LEDPin, NewState):  # Turns a LED on or off
	if NewState == "HIGH":
		GPIO.output(LEDPin, GPIO.HIGH)
	elif NewState == "LOW":
		GPIO.output(LEDPin, GPIO.LOW)
	else:
		print("Error, invalid state.")


def Buzzer(i):  # Buzzes for i amount of seconds
	GPIO.output(BuzzerPin, GPIO.HIGH)
	time.sleep(i)
	GPIO.output(BuzzerPin, GPIO.LOW)


def LEDOnOff(LEDPin): #Turns a LED on and off
	GPIO.output(LEDPin, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(LEDPin, GPIO.LOW)


def ChooseRandomLED():  # Chooses a random LED
	global RandomPin 
	RandomLED = random.randint(1, 3)
	if RandomLED == 1:
		print(str(1))
		RandomPin = 18
	elif RandomLED == 2:
		print(str(2))
		RandomPin = 23
	elif RandomLED == 3:
		print(str(3))
		RandomPin = 24


def ButtonLoop():  # The while loop for the button
	while True:
		try:
			if GPIO.input(ButtonPin) == False:
				ChooseRandomLED()
				LEDOnOff(RandomPin)
#				time.sleep(1)
#			else:
#				LED(RandomPin, "LOW")
#				time.sleep(1)
		except KeyboardInterrupt:
			GPIO.cleanup()

ButtonLoop()
