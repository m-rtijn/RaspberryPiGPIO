# Made by: MrTijn/Tijndagamer
# Copyright 2015

from ADXL345 import ADXL345

#Create an instance of the ADXL345 class
accelerometer = ADXL345(0x53)

while True:
    axes = accelerometer.GetAllAxes()
    print("x: %.3f" %(axes['x'])
    print("y: %.3f" %(axes['y']))
    print("z: %.3f" %(axes['z'])) 
