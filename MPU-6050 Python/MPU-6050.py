# This program handles the communication over I2C
# between a Raspberry Pi and a MPU-6050 Gyroscope / Accelerometer combo
# Made by: MrTijn/Tijndagamer
# Copyright 2015

import smbus

class MPU6050:

    # Global Variables
    address = None
    scaleMultiplier2G = 16384

    # MPU-6050 Registers
    
    ACCEL_XOUT0 = 0x3B
    ACCEL_XOUT1 = 0x3C
    ACCEL_YOUT0 = 0x3D
    ACCEL_YOUT1 = 0x3E
    ACCEL_ZOUT0 = 0x3F
    ACCEL_ZOUT1 = 0x40

    TEMP_OUT0 = 0x41
    TEMP_OUT1 = 0x42

    GYRO_XOUT0 = 0x43
    GYRO_XOUT1 = 0x44
    GYRO_YOUT0 = 0x45
    GYRO_YOUT1 = 0x46
    GYRO_ZOUT0 = 0x47
    GYRO_ZOUT1 = 0x48

    def __init__(self, address):
        self.address = address

    # Returns the temperature in degrees celcius
    def GetTemperature(self):
        # Todo: Add this
        pass

    # Sets the range of the accelerometer to range
    def SetAccelRange(self, range):
        # Todo: Add this
        pass

    # Reads the range the accelerometer is set to
    def ReadAccelRange(self):
        # Todo: Add this
        pass

    # Gets and returns the X, Y and Z values from the accelerometer
    def GetAllAccelValues(self):
        # Todo: Add this
        pass

    # Sets the range of the gyroscope to range
    def SetGyroRange(self, range):
        # Todo: Add this
        pass

    # Reads the range the gyroscope is set to
    def ReadGyroRange(self):
        # Todo: Add this
        pass

    # Gets and returns the X, Y and Z values from the gyroscope
    def GetAllGyroValues(self):
        # Todo: Add this
        pass

    # Gets and returns the X, Y and Z values from the accelerometer and from the gyroscope and the temperature from the temperature sensor
    def GetAllValues(self):
        # Todo: Add this
        pass
