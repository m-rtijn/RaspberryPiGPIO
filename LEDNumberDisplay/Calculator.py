#Import libraries
import os
import sys

def PrintOutput(output):
#	print(output)
	outputList = map(int, str(output))
	for digit in outputList:
#		print(digit)
		os.system("sudo python NumberPrinter.py " + str(digit) + " 1")

def ArgumentHandler():
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
