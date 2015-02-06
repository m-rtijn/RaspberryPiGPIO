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

    # Pre-defined ranges
    accelRange2G = 0x00
    accelRange4G = 0x08
    accelRange8G = 0x10
    accelRange16G = 0x18

    gyroRange250Deg = 0x00
    gyroRange500Deg = 0x08
    gyroRange1000Deg = 0x10
    gyroRange2000Deg = 0x18

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

    ACCEL_CONFIG = 0x1C
    GYRO_CONFIG = 0x1B

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

    # Returns the temperature in degrees celcius read from the temperature sensor in the MPU-6050
    def GetTemp(self):
        # Get the raw data
        rawTemp = self.ReadI2CWord(self.TEMP_OUT0)

        # Get the actual temperature using the formule given in the
        # MPU-6050 Register Map and Descriptions revision 4.2, page 30
        actualTemp = (rawTemp / 340) + 36.53

        # Return the temperature
        return actualTemp

    # Sets the range of the accelerometer to range
    def SetAccelRange(self, accelRange):
        # First change it to 0x00 to make sure we write the correct value later
        self.bus.write_byte_data(self.address, self.ACCEL_CONFIG, 0x00)

        # Write the new range to the ACCEL_CONFIG register
        self.bus.write_byte_data(self.address, self.ACCEL_CONFIG, accelRange)

    # Reads the range the accelerometer is set to
    # If raw is True, it will return the raw value
    # If raw is False, it will return an integer: -1, 2, 4, 8 or 16. When it returns -1 something went wrong.
    def ReadAccelRange(self, raw = False):
        # Get the raw value
        rawData = self.bus.read_byte_data(self.address, self.ACCEL_CONFIG)

        if raw is True:
            return rawData
        elif raw is False:
            if rawData == self.accelRange2G:
                return 2
            elif rawData == self.accelRange4G:
                return 4
            elif rawData == self.accelRange8G:
                return 8
            elif rawData == self.accelRange16G:
                return 16
            else:
                return -1

    # Gets and returns the X, Y and Z values from the accelerometer
    def GetAccelValues(self):
        # Read the data from the MPU-6050
        x = self.ReadI2CWord(self.ACCEL_XOUT0)
        y = self.ReadI2CWord(self.ACCEL_YOUT0)
        z = self.ReadI2CWord(self.ACCEL_ZOUT0)

        scaleMultiplier = None
        accelRange = self.ReadAccelRange(True)

        if accelRange == self.accelRange2G:
            accelScaleMultiplier = self.accelScaleMultiplier2G
        elif accelRange == self.accelRange4G:
            accelScaleMultiplier = self.accelScaleMultiplier4G
        elif accelRange == self.accelRange8G:
            accelScaleMultiplier = self.accelScaleMultiplier8G
        elif accelRange == self.accelRange16G:
            accelScaleMultiplier = self.accelScaleMultiplier16G
        else:
            print("Unkown range - accelScaleMultiplier set to self.accelScaleMultiplier2G")
            accelScaleMultiplier = self.accelScaleMultiplier2G
        
        x = x / accelScaleMultiplier
        y = y / accelScaleMultiplier
        z = z / accelScaleMultiplier

        return {'x': x, 'y': y, 'z': z}

    # Sets the range of the gyroscope to range
    def SetGyroRange(self, range):
        # First change it to 0x00 to make sure we write the correct value later
        self.bus.write_byte_data(self.address, self.GYRO_CONFIG, 0x00)

        # Write the new range to the ACCEL_CONFIG register
        self.bus.write_byte_data(self.address, self.GYRO_CONFIG, accelRange)

    # Reads the range the gyroscope is set to
    def ReadGyroRange(self, raw = False):
        # Get the raw value
        rawData = self.bus.read_byte_data(self.address, self.GYRO_CONFIG)

        if raw is True:
            return rawData

    # Gets and returns the X, Y and Z values from the gyroscope
    def GetGyroValues(self):
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
        temp = GetTemp()
        accel = GetAllAccelValues()
        gyro = GetAllGyroValues()

        return [accel, gyro, temp]
