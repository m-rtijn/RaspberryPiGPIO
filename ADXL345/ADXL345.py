"""This program handles the communication over I2C between a Raspberry Pi and an ADXL345 Accelerometer
Made by: MrTijn/Tijndagamer
Copyright 2015
"""

import smbus


class ADXL345:
    """A class that is used to create an instance of the ADXL345,
    so the user can interact with the device
    """

    # Global Variables
    earthGravityMS2 = 9.80665
    moonGravityMS2 = 1.62243
    marsGravityMS2 = 3.71
    gravityMS2 = None
    scaleMultiplier = 0.0039  # Typical scale factor in g/LSB (http://goo.gl/FFuYV0, page 4)
    bus = smbus.SMBus(1)  # This is the bus that we use to send data over I2C
    address = None
    DEBUG = False

    # ADXL345 Registers
    dataFormat = 0x31
    bandwithRate = 0x2C
    POWER_CTL = 0x2D
    measure = 0x08

    bandwithRate1600HZ = 0x0F
    bandwithRate800HZ = 0x0E
    bandwithRate400HZ = 0x0D
    bandwithRate200HZ = 0x0C
    bandwithRate100HZ = 0x0B
    bandwithRate50HZ = 0x0A
    bandwithRate25HZ = 0x09
    range2G = 0x00
    range4G = 0x01
    range8G = 0x02
    range16G = 0x03

    DATAX0 = 0x32
    DATAX1 = 0x33
    DATAY0 = 0x34
    DATAY1 = 0x35
    DATAZ0 = 0x36
    DATAZ1 = 0x37

    def __init__(self, address, baseRange=range2G, baseBandwithRate=bandwithRate100HZ, celestialBody="earth"):
        """The initializing function that sets several default values for the device,
        and assigns it the correct properties
        """

        if celestialBody == "earth":
            self.gravityMS2 = self.earthGravityMS2

        elif celestialBody == "moon":
            self.gravityMS2 = self.moonGravityMS2

        elif celestialBody == "mars":
            self.gravityMS2 = self.marsGravityMS2

        else:
            raise InputError("celestial body", celestialBody)

        self.address = address
        self.SetBandwithRate(baseBandwithRate)
        self.SetRange(baseRange)
        self.EnableMeasurement()

    def EnableMeasurement(self):
        """This tries to send a signal to the device that
        tells it to turn on and start measuring
        Happens by writing 0x08 to POWER_CTL, register 0x27
        """

        try:
            self.bus.write_byte_data(self.address, self.POWER_CTL, self.measure)

        except:
            print("Error in EnableMeasurement(), are you sure that the ADXL345 is plugged in and wired correctly?")

    def DisableMeasurement(self):
        """This tries to send a signal to the device
        that tells it to stop measuring.
        Uses register 0x27, and sends 0x00 to POWER_CTL
        """

        self.bus.write_byte_data(self.address, self.POWER_CTL, 0x00)

    def ReadMeasurementMode(self):
        """This sends a signal to the device that tells it to go into read mode,
        so the user can extract data.
        Uses register 0x27 and reads POWER_CTL
        """

        return self.bus.read_byte_data(self.address, self.POWER_CTL)

    def SetBandwithRate(self, rate):
        """This sets the bandwithRate to whatever the user specifies.
        Uses register 0x2C
        """

        try:
            self.bus.write_byte_data(self.address, self.bandwithRate, rate)

        except:
            print("Error in SetBandwithRate, are you sure that the ADXL345 is plugged in and wired correctly?")

    def ReadBandwithRate(self):
        """This retrieves the bandwithRate from the device,
        and returns it to the user
        Using register 0x2C
        """

        rawBandwithRate = self.bus.read_byte_data(self.address, self.bandwithRate)

        return rawBandwithRate & 0x0F

    def SetRange(self, range):
        """Set the range. Available options are 2G, 4G, 8G and 16G"""

        value = self.bus.read_byte_data(self.address, self.dataFormat)

        value &= ~0x0F
        value |= range
        value |= 0x08

        self.bus.write_byte_data(self.address, self.dataFormat, value)

    def ReadRange(self):
        """Reads the range the ADXL345 is set to.
        PS: This function is still a WIP
        """

        rawValue = self.bus.read_byte_data(self.address, self.dataFormat)

        return rawValue

    def GetAllAxes(self, round=False):
        """Gets all the axes and returns them in a dictionary
        As of right now it is unknown how the byte things under work
        The scale multiplier is given in the datasheet.
        """

        # Read the raw bytes from the ADXL345
        bytes = self.bus.read_i2c_block_data(self.address, self.DATAX0, 6)

        x = bytes[0] | (bytes[1] << 8)  # From this line
        if(x & (1 << 16 - 1)):
            x = x - (1 << 16)

        y = bytes[2] | (bytes[3] << 8)
        if(y & (1 << 16 - 1)):
            y = y - (1 << 16)

        z = bytes[4] | (bytes[5] << 8)
        if(z & (1 << 16 - 1)):
            z = z - (1 << 16)  # To this line we're not completly sure what's happening

        # Multiply the values by the scale multiplier to get the acceleration in g
        x = x * self.scaleMultiplier
        y = y * self.scaleMultiplier
        z = z * self.scaleMultiplier

        # Multiply the values in g by the gravity in m/s^2 to get the acceleration in m/s^2
        x = x * self.gravityMS2
        y = y * self.gravityMS2
        z = z * self.gravityMS2

        # Round the values if the user wants to
        if round:
            x = round(x, 4)
            y = round(y, 4)
            z = round(z, 4)

        # Return the correct values
        if not self.DEBUG:
            return {"x": x, "y": y, "z": z}

        elif self.DEBUG:
            return {"x": x, "y": y, "z": z, "bytes": bytes}

        else:
            return {"x": x, "y": y, "z": z}

    def GetOneValue(self, value, round=False):
        """Retrieves one specific value and returns it
        Once again we do not yet understand the byte things"""

        readRegister = 0x00

        if value == "x":
            readRegister = self.DATAX0

        elif value == "y":
            readRegister = self.DATAY0

        elif value == "z":
            readRegister = self.DATAZ0

        # Read the raw bytes from the ADXL345
        bytes = self.bus.read_i2c_block_data(self.address, readRegister, 2)

        x = bytes[0] | (bytes[1] << 8)  # Unknown from here
        if(x & (1 << 16 - 1)):
            x = x - (1 << 16)  # to here

        # Multiply the value by the scale multiplier to get the acceleration in g. The scale multiplier is given in the datasheet.
        x = x * self.scaleMultiplier

        # Multiply the value in g by the gravity in m/s^2 to get the acceleration in m/s^2.
        x = x * self.gravityMS2

        # Round the values if the user wants to
        if round:
            x = round(x, 4)

        return x


if __name__ == "__main__":

    accelerometer = ADXL345()
    axes = accelerometer.GetAllAxes()

    print("x: %.3f" % (axes['x']))
    print("y: %.3f" % (axes['y']))
    print("z: %.3f" % (axes['z']))


class InputError(Exception):
    """This provides instructions for an instance of an error"""

    def __init__(self, errorMessage, inputExpression):
        self.errorMessage = errorMessage
        self.inputExpression = inputExpression
        print(inputExpression + " is an invalid " + errorMessage)
