"""This program prints numbers
Made by: MrTijn/Tijndagamer
Copyright 2015
"""

import RPi.GPIO as GPIO
import time
import sys

# Setup the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup the LED pins as output
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

# The NumberLists
list0 = [18, 27, 24, 25, 22, 17]
list1 = [24, 18]
list2 = [25, 18, 23, 22, 27]
list3 = [25, 18, 23, 24, 27]
list4 = [17, 23, 18, 24]
list5 = [25, 17, 23, 24, 27]
list6 = [25, 17, 23, 22, 24, 27]
list7 = [25, 18, 24]
list8 = [25, 17, 18, 23, 22, 24, 27]
list9 = [25, 17, 18, 23, 24, 27]

"""This function turns all the pins in the specified numberList to high for variable onTime time.
numberList: this is the list with GPIO pin numbers that should be turned on
onTime: the time the GPIO pins will be set to GPIO.HIGH
"""


def PrintNumber(numberList, onTime):
	for pin in numberList:
		GPIO.output(pin, GPIO.HIGH)
	time.sleep(onTime)
	for pin in numberList:
		GPIO.output(pin, GPIO.LOW)


def ArgumentHandler():  # This functions handles the arguments given in the commandline
	if sys.argv[1] == "0":
		PrintNumber(list0, int(sys.argv[2]))
	if sys.argv[1] == "1":
		PrintNumber(list1, int(sys.argv[2]))
	if sys.argv[1] == "2":
		PrintNumber(list2, int(sys.argv[2]))
	if sys.argv[1] == "3":
		PrintNumber(list3, int(sys.argv[2]))
	if sys.argv[1] == "4":
		PrintNumber(list4, int(sys.argv[2]))
	if sys.argv[1] == "5":
		PrintNumber(list5, int(sys.argv[2]))
	if sys.argv[1] == "6":
		PrintNumber(list6, int(sys.argv[2]))
	if sys.argv[1] == "7":
		PrintNumber(list7, int(sys.argv[2]))
	if sys.argv[1] == "8":
		PrintNumber(list8, int(sys.argv[2]))
	if sys.argv[1] == "9":
		PrintNumber(list9, int(sys.argv[2]))
	elif sys.argv[1] == "help":
		print("Usage: sudo python NumberPrinter.py [number] [seconds on]")


try:
	ArgumentHandler()
	GPIO.cleanup()

except KeyboardInterrupt:
	GPIO.cleanup()
