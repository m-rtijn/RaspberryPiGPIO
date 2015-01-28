"""Created by MrTijn/Tijndagamer
Counts how long a button is pressed
Copyright 2014
"""

import RPi.GPIO as GPIO
import time

# Setup the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ButtonPin1 = 22
ButtonPin2 = 27

GPIO.setup(ButtonPin1, GPIO.IN)
GPIO.setup(ButtonPin2, GPIO.IN)


def MeasurePress(ButtonPin):
    while GPIO.input(ButtonPin) == 1:
        pass
    start = time.time()

    while GPIO.input(ButtonPin) == 0:
        pass
    stop = time.time()

    return stop - start


while True:
    print(MeasurePress(ButtonPin1))
