import RPi.GPIO as GPIO
import time

# Global Variables
ECHO = 24
TRIG = 25

# Setup the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(TRIG, GPIO.LOW)

GPIO.setup(ECHO, GPIO.IN)

# Returns the range in CM or M
# If returnFormat is True, it will return in CM
# If returnFormat is False, it will return in M
def MeasureRange(returnFormat):
    # First sleep to make sure that we aren't overloading the HC-SR04
    time.sleep(0.1)

    # Send the trigger signal
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    # Listen to the ECHO pin
    while GPIO.input(ECHO) == 0:
        pass
    start = time.time()

    while GPIO.input(ECHO) == 1:
        pass
    stop = time.time()

    # Check what to return
    if (returnFormat is True):
        return (stop - start) * 17000
    if (returnFormat is False):
        return (stop - start) * 170

while True:
    print(str(MeasureRange(True)) + " cm")
