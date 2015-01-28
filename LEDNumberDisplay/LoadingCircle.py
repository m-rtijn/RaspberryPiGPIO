"""Created by MrTijn/Tijndagamer
Copyright 2015
"""

import RPi.GPIO as GPIO
import time
import sys

# Setup the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the pin variables
LEDpin_1 = 24
LEDpin_2 = 18
LEDpin_3 = 25
LEDpin_4 = 17
LEDpin_5 = 22
LEDpin_6 = 27

# Setup the pins
GPIO.setup(LEDpin_1, GPIO.OUT)
GPIO.setup(LEDpin_2, GPIO.OUT)
GPIO.setup(LEDpin_3, GPIO.OUT)
GPIO.setup(LEDpin_4, GPIO.OUT)
GPIO.setup(LEDpin_5, GPIO.OUT)
GPIO.setup(LEDpin_6, GPIO.OUT)

# Other variables
i = 2


def OnAndOff(pin):
	# print(str(pin))
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(i)
	GPIO.output(pin, GPIO.LOW)


while True:
	try:
		OnAndOff(LEDpin_1)
		OnAndOff(LEDpin_2)
		OnAndOff(LEDpin_3)
		OnAndOff(LEDpin_4)
		OnAndOff(LEDpin_5)
		OnAndOff(LEDpin_6)

        if i > 0:
			i = i - 0.25
		else:
			print("i is to small. i = " + str(i))
			GPIO.cleanup()
			sys.exit()

    except KeyboardInterrupt:
		GPIO.cleanup()
