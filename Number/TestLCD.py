import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinList = [17, 18, 23, 22, 24, 25, 27]

for pin in pinList:
	print(str(pin) + " is now output")
	GPIO.setup(pin, GPIO.OUT)

for pin in pinList:
	GPIO.output(pin, GPIO.HIGH)
	print(str(pin) + " is now HIGH")
	time.sleep(3)

GPIO.cleanup()
