# This program handles the communication over I2C
# between a Raspberry Pi and a MPU-6050 Gyroscope / Accelerometer combo
# Made by: MrTijn/Tijndagamer
# Copyright 2015

import smbus

class MPU6050:

    # Global Variables
    address = None
    bus = smbus.SMBus(1)

    # Scale multipliers
    accelScaleMultiplier2G = 16384.0
    accelScaleMultiplier4G = 8192.0
    accelScaleMultiplier8G = 4096.0
    accelScaleMultiplier16G = 2048.0
    gyroScaleMultiplier250Deg = 131.0
    gyroScaleMultiplier500Deg = 65.5
    gyroScaleMultiplier1000Deg = 32.8
    gyroScaleMultiplier2000Deg = 16.4

    # MPU-6050 Registers
    PWR_MGMT_1 = 0x6B
    PWR_MGMT_2 = 0x6C
    
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

        # Wake up the MPU-6050 since it starts in sleep mode
        self.bus.write_byte_data(self.address, self.PWR_MGMT_1, 0x00)

    # I2C communication methods

    def ReadI2CWord(self, register):
        # Read the data from the registers
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)

        # Bit magic
        value = (high << 8) + low

        if (value >= 0x8000):
            return -((65535 - value) + 1)
        else:
            return value

    # MPU-6050 Methods

    # Returns the temperature in degrees celcius.
    def GetTemp(self):
        # Get the raw data
        rawTemp = self.ReadI2CWord(self.TEMP_OUT0)

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
        # Read the data from the MPU-6050
        x = self.ReadI2CWord(self.ACCEL_XOUT0)
        y = self.ReadI2CWord(self.ACCEL_YOUT0)
        z = self.ReadI2CWord(self.ACCEL_ZOUT0)

        # TODO: Add options to use the correct scale multiplier for the current range
        x = x / self.accelScaleMultiplier2G
        y = y / self.accelScaleMultiplier2G
        z = z / self.accelScaleMultiplier2G

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
        # Read the raw data from the MPU-6050
        x = self.ReadI2CWord(self.GYRO_XOUT0)
        y = self.ReadI2CWord(self.GYRO_YOUT0)
        z = self.ReadI2CWord(self.GYRO_ZOUT0)

        # TODO: Add options to use the correct scale multiplier for the current range
        x = x / self.gyroScaleMultiplier250Deg
        y = y / self.gyroScaleMultiplier250Deg
        z = z / self.gyroScaleMultiplier250Deg

        return {'x': x, 'y': y, 'z': z}      

    # Gets and returns the X, Y and Z values from the accelerometer and from the gyroscope and the temperature from the temperature sensor
    def GetAllValues(self):
        # Todo: Add this
        pass
