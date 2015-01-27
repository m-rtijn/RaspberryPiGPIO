"""This program handles the communication between a Raspberry Pi and an HC-SR04 Ultrasonic range finder
Made by: MrTijn/Tijndagamer
Copyright 2015
"""

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


def MeasureRange(returnFormat):
    """Returns the range in CM or M
    If returnFormat is True, it will return in CM
    If returnFormat is False, it will return in M
    """

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
    if returnFormat:
        return (stop - start) * 17000

    if not returnFormat:
        return (stop - start) * 170

while True:
    print(str(MeasureRange(True)) + " cm")
