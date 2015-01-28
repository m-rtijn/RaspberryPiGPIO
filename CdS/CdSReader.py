#Most of this code is copied from this tutorial: https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi?view=all

#Importing the libraries
import RPi.GPIO as GPIO
import time

#Setup the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Reads the CdS cel and returns the reading
def ReadCdSCel(CdSCelPin):
	reading = 0
	GPIO.setup(CdSCelPin, GPIO.OUT)
	GPIO.output(CdSCelPin, GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(CdSCelPin, GPIO.IN)
	while (GPIO.input(CdSCelPin) == GPIO.LOW):
		reading += 1
	return reading

while True:
	print ReadCdSCel(18)
