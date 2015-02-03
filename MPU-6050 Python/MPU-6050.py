# This program handles the communication over I2C
# between a Raspberry Pi and a MPU-6050 Gyroscope / Accelerometer combo
# Made by: MrTijn/Tijndagamer
# Copyright 2015

import smbus

class MPU6050:

    # Global Variables
    address = None
    bus = smbus.SMBus(1)
    scaleMultiplier2G = 16384.0

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
         rawValues = self.bus.read_i2c_block_data(self.address, self.TEMP_OUT0, 2)

         rawTemp = rawValues[0] | (rawValues[1] << 8)

         # Get the actual temperature using the formule given in the MPU-6050 Register Map and Descriptions revision 4.2, page 30
         actualTemp = (rawTemp / 340) + 36.53

         # Return the temperature
         return actualTemp

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
        rawValues = self.bus.read_i2c_block_data(self.address, self.ACCEL_XOUT0, 6)

        x = rawValues[0] | (rawValues[1] << 8)
        y = rawValues[2] | (rawValues[3] << 8)
        z = rawValues[4] | (rawValues[5] << 8)

        # TODO: Add options to use the correct scale multiplier for the current range
        x = x / scaleMultiplier2G
        y = y / scaleMultiplier2G
        z = z / scaleMultiplier2G

        return {'x': x, 'y': y, 'z': z}
        

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
