"""Created by MrTijn/Tijndagamer
Copyright 2015
"""

# Import libraries
import os
import sys


def PrintOutput(output):
    """Prints something specified by the user"""

	outputList = map(int, str(output))
	
    for digit in outputList:
		os.system("sudo python NumberPrinter.py " + str(digit) + " 1")


def ArgumentHandler():
    """Handles the arguments passed to the script"""

	if sys.argv[2] == "+":
		PrintOutput(int(sys.argv[1]) + int(sys.argv[3]))
	if sys.argv[2] == "-":
		PrintOutput(int(sys.argv[1]) - int(sys.argv[3]))
	if sys.argv[2] == "*":
		PrintOutput(int(sys.argv[1]) * int(sys.argv[3]))
	if sys.argv[2] == ":" or sys.argv[2] == "/":
		PrintOutput(int(sys.argv[1]) / int(sys.argv[3]))
	if sys.argv[1] == "help":
		print("usage: sudo python Calculator.py [a] [operator] [b]")

ArgumentHandler()
