"""Created by MrTijn/Tijndagamer
Control the GPIO
Copyright 2014
"""

# Importing libraries
import sys
import time
import RPi.GPIO as GPIO

# Setup the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def SetupOutput(Pin): #Setups a pin as an output pin
	GPIO.setup(Pin, GPIO.OUT)
	print("The pin " + str(Pin) + " is now an output pin")


#def SetupInput(Pin): #Setups a pin as an input pin
#	GPIO.setup(Pin, GPIO.IN)
#	print("The pin " + str(Pin) + " is now an input pin")


def SetHigh(Pin): #Sets a pin high
	SetupOutput(Pin)
	GPIO.output(Pin, GPIO.HIGH)


def SetLow(Pin):
	SetupOutput(Pin)
	GPIO.output(Pin, GPIO.LOW)


def main():
	print("Use: sudo python Control.py [pinnumber] [state]")
	# First check if there are enough arguments

    if len(sys.argv) == 3:
		if sys.argv[2] == "HIGH":
			# First convert argv[1] to an int
			param = int(sys.argv[1])
			# Call SetHigh to set the pin high
			SetHigh(param)
		if sys.argv[2] == "LOW":
			# First convert argv[1] to an int
			param = int(sys.argv[1])
			# Call SetLow to set the pin low
			SetLow(param)
		if sys.argv[1] == "cleanup":
			print("Cleaning up this mess")
			GPIO.cleanup()
		else:
			print("Error, reached else statement. exiting script [1]")
			GPIO.cleanup()
			sys.exit()
	else:
		print("Error, reached else statement. exiting script [0]")

        GPIO.cleanup()
		sys.exit()


main()
GPIO.cleanup()
