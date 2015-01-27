# This program handles the communication over I2C between a Raspberry Pi and an ADXL345 Accelerometer
# Made by: MrTijn/Tijndagamer
# Copyright 2015

import smbus

class ADXL345:

    # Global Variables
    earthGravityMS2               = 9.80665
    moonGravityMS2                = 1.62243
    marsGravityMS2                = 3.71
    gravityMS2                    = None
    scaleMultiplier               = 0.0039 # This is the typical scale factor in g/LSB as given in the datasheet (http://www.analog.com/static/imported-files/data_sheets/ADXL345.pdf , page 4) 
    bus                           = smbus.SMBus(1)
    address                       = None
    DEBUG                         = False

    # ADXL345 Registers
    dataFormat                    = 0x31
    bandwithRate                  = 0x2C
    POWER_CTL                     = 0x2D
    measure                       = 0x08

    bandwithRate1600HZ            = 0x0F
    bandwithRate800HZ             = 0x0E
    bandwithRate400HZ             = 0x0D
    bandwithRate200HZ             = 0x0C
    bandwithRate100HZ             = 0x0B
    bandwithRate50HZ              = 0x0A
    bandwithRate25HZ              = 0x09

    range2G                       = 0x00
    range4G                       = 0x01
    range8G                       = 0x02
    range16G                      = 0x03

    DATAX0                        = 0x32
    DATAX1                        = 0x33
    DATAY0                        = 0x34
    DATAY1                        = 0x35
    DATAZ0                        = 0x36
    DATAZ1                        = 0x37
    
    def __init__(self,  address, baseRange = range2G, baseBandwithRate = bandwithRate100HZ, celestialBody = "earth"):
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

    # Enables measurement by writing 0x08 to POWER_CTL, register 0x27
    def EnableMeasurement(self):
        try:
            self.bus.write_byte_data(self.address, self.POWER_CTL, self.measure)
        except:
            print("Error in EnableMeasurement(), are you sure that the ADXL345 is plugged in and wired correctly?")

    # Disables measurement by writing 0x00 to POWER_CTL, register 0x27
    def DisableMeasurement(self):
        self.bus.write_byte_data(self.address, self.POWER_CTL, 0x00)

    # Reads POWER_CTL, register 0x27
    def ReadMeasurementMode(self):
        return self.bus.read_byte_data(self.address, self.POWER_CTL) 

    # Changes the bandwithRate by writing rate to bandwithRate, register 0x2C
    def SetBandwithRate(self, rate):
        try:
            self.bus.write_byte_data(self.address, self.bandwithRate, rate)
        except:
            print("Error in SetBandwithRate, are you sure that the ADXL345 is plugged in and wired correctly?")

    # Reads bandwithRate, register 0x2C
    def ReadBandwithRate(self):
        rawBandwithRate = self.bus.read_byte_data(self.address, self.bandwithRate)
        return rawBandwithRate & 0x0F

    # Changes the range of the ADXL345. Available ranges are 2G, 4G, 8G and 16G.
    def SetRange(self, range):
        value = self.bus.read_byte_data(self.address, self.dataFormat)

        value &= ~0x0F;
        value |= range;
        value |= 0x08;

        self.bus.write_byte_data(self.address, self.dataFormat, value)

    # Reads the range the ADXL345 is set to. This function is still a WIP
    def ReadRange(self):
        rawValue = self.bus.read_byte_data(self.address, self.dataFormat)

        return rawValue

    # Gets all the axes and returns them in a dictionary
    def GetAllAxes(self, round = False):
        # Read the raw bytes from the ADXL345
        bytes = self.bus.read_i2c_block_data(self.address, self.DATAX0, 6)

        #<~~magic~~>
        x = bytes[0] | (bytes[1] << 8)
        if(x & (1 << 16 - 1)):
            x = x - (1<<16)
        
        y = bytes[2] | (bytes[3] << 8)
        if(y & (1 << 16 - 1)):
            y = y - (1<<16)

        z = bytes[4] | (bytes[5] << 8)
        if(z & (1 << 16 - 1)):
            z = z - (1<<16)

        x = x * self.scaleMultiplier 
        y = y * self.scaleMultiplier
        z = z * self.scaleMultiplier
        #</~~magic~~>

        x = x * self.gravityMS2
        y = y * self.gravityMS2
        z = z * self.gravityMS2

        if round == True:
            x = round(x, 4)
            y = round(y, 4)
            z = round(z, 4)

        if self.DEBUG == False:
            return {"x": x, "y": y, "z": z}
        elif self.DEBUG == True:
            return {"x": x, "y": y, "z": z, "bytes": bytes}
        else:
            return {"x": x, "y": y, "z": z}

    #Gets one specific value and returns it
    def GetOneValue(self, value, round = False):
        readRegister = 0x00
        
        if value == "x":
            readRegister = self.DATAX0
        elif value == "y":
            readRegister = self.DATAY0
        elif value == "z":
            readRegister = self.DATAZ0
            
        #Read the raw bytes from the ADXL345
        bytes = self.bus.read_i2c_block_data(self.address, readRegister, 2)

        #<~~magic~~>
        x = bytes[0] | (bytes[1] << 8)
        if(x & (1 << 16 - 1)):
            x = x - (1<<16)

        x = x * self.scaleMultiplier

        x = x * self.gravityMS2
        #</~~magic~~>

        if round == True:
            x = round(x, 4)
        
        return x
    
if __name__ == "__main__":
    accelerometer = ADXL345()
    axes = accelerometer.GetAllAxes()
    print("x: %.3f" % ( axes['x'] ))
    print("y: %.3f" % ( axes['y'] ))
    print("z: %.3f" % ( axes['z'] ))
        

class InputError(Exception):

    def __init__(self, errorMessage, inputExpression):
        self.errorMessage = errorMessage
        self.inputExpression = inputExpression
        print(inputExpression + " is an invalid " + errorMessage)
