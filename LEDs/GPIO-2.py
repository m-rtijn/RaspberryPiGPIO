"""Created by MrTijn/Tijndagamer
Interaction with the GPIO
"""

import RPi.GPIO as GPIO
import time

# Setup the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup the Button
ButtonPin = int(raw_input("ButtonPin ="))
GPIO.setup(ButtonPin, GPIO.IN)

# Setup the LED
LEDPin = int(raw_input("LEDPin ="))
GPIO.setup(LEDPin, GPIO.OUT)

# Setup the Buzzer
# BuzzerPin = int(raw_input("BuzzerPin ="))
# GPIO.setup(BuzzerPin, GPIO.OUT)


def LED(NewState):  # Turns the LED on or off
	if NewState == "HIGH":
		GPIO.output(LEDPin, GPIO.HIGH)
	elif NewState == "LOW":
		GPIO.output(LEDPin, GPIO.LOW)
	else:
		print("Error, invalid state")


def Buzzer(i):  # Buzzes for i*seconds
	GPIO.output(BuzzerPin, GPIO.HIGH)
	time.sleep(i)
	GPIO.output(BuzzerPin, GPIO.LOW)


def ButtonLoop():  # The while loop for the button
	while True:
		try:
			if GPIO.input(ButtonPin) == False:
				LED("HIGH")
#				Buzzer(0.001)
			else:
				LED("LOW")
		except KeyboardInterrupt:
			GPIO.cleanup()


ButtonLoop()
