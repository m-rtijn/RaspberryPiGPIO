import RPi.GPIO as GPIO
import time
import sys

#Setup the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def main():
	if sys.argv[1] == "help":
		print("sudo python blink.py <pinnumber> <time in seconds>")
		sys.exit()
	GPIO.setup(int(sys.argv[1]), GPIO.OUT)
	GPIO.output(int(sys.argv[1]), GPIO.HIGH)
	time.sleep(int(sys.argv[2]))
	GPIO.output(int(sys.argv[1]), GPIO.LOW)
	GPIO.cleanup()

#for i in sys.argv:
#	print(i)
main()
GPIO.cleanup()
