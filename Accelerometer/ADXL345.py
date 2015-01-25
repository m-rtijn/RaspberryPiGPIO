#This program handles the communication over I2C between a Raspberry Pi and an ADXL345 Accelerometer
#Made by: MrTijn/Tijndagamer
#Copyright 2015

import smbus

class MrTijnADXL345:

    #Global Variables
    earthGravityMS2               = 9.80665
    moonGravityMS2                = 1.62243
    marsGravityMS2                = 3.71
    gravityMS2                    = 0
    scaleMultiplier               = 0.004
    bus                           = smbus.SMBus(1)
    address                       = None

    #ADXL345 Registers
    dataFormat                    = 0x31
    bandwithRate                  = 0x2C
    POWER_CTL                     = 0x2D

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

    Measure                       = 0x08

    DATAX0                        = 0x32
    DATAX1                        = 0x33
    DATAY0                        = 0x34
    DATAY1                        = 0x35
    DATAZ0                        = 0x36
    DATAZ1                        = 0x37
    
    def __init__(self, baseRange = range2G, address = 0x52, celestialBody = "earth"):
        if celestialBody == "earth":
            self.gravityMS2 = self.earthGravityMS2
        elif celestialBody == "moon":
            self.gravityMS2 = self.moonGravityMS2
        elif celestialBody == "mars":
            self.gravityMS2 = self.marsGravityMS2
        else:
            raise InputError("celestial body", celestialBody)

        self.address = address
        self.SetBandwithRate(self.bandwithRate100HZ)
        self.SetRange(baseRange)
        self.EnableMeasurement()

    #Enables measurement by writing 0x08 to POWER_CTL, register 0x27
    def EnableMeasurement(self):
        try:
            self.bus.write_byte_data(self.address, self.POWER_CTL, self.Measure)
        except:
            print("Error in EnableMeasurement(), are you sure that the ADXL345 is plugged in and wired correctly?")

    #Disables measurement by writing 0x00 to POWER_CTL, register 0x27
    def DisableMeasurement(self):
        self.bus.write_byte_data(self.address, self.POWER_CTL, 0x00)

    #Reads POWER_CTL, register 0x27
    def ReadMeasurementMode(self):
        return self.bus.read_byte_data(self.address, self.POWER_CTL) 

    #Changes the bandwithRate by writing rate to bandwithRate, register 0x2C
    def SetBandwithRate(self, rate):
        self.bus.write_byte_data(self.address, self.bandwithRate, rate)

    #Reads bandwithRate, register 0x2C
    def ReadBandwithRate(self):
        rawBandwithRate = self.bus.read_byte_data(self.address, self.bandwithRate)
        return rawBandwithRate & 0x0F

    #Changes the range of the ADXL345. Available ranges are 2G, 4G, 8G and 16G.
    def SetRange(self, range):
        value = self.bus.read_byte_data(self.address, self.dataFormat)

        value &= ~0x0F;
        value |= range;
        value |= 0x08;

        self.bus.write_byte_data(self.address, self.dataFormat, value)

    #Reads the range the ADXL345 is set to.
    def ReadRange(self):
        #todo
        pass

    #Gets all the axes and returns them in a dictionary
    def GetAllAxes(self, round = False):
        #Read the raw bytes from the ADXL345
        bytes = self.bus.read_i2c_block_data(self.address, self.DATAX0, 6)
        
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

        x = x * self.gravityMS2
        y = y * self.gravityMS2
        z = z * self.gravityMS2

        if round == True:
            x = round(x, 4)
            y = round(y, 4)
            z = round(z, 4)

        return {"x": x, "y": y, "z": z}

if __name__ == "__main__":
    accel = MrTijnADXL345()
    axes = accel.GetAllAxes()
    print("x: %.3f" % ( axes['x'] ))
    print("y: %.3f" % ( axes['y'] ))
    print("z: %.3f" % ( axes['z'] ))
        

class InputError(Exception):

    def __init__(self, errorMessage, inputExpression):
        self.errorMessage = errorMessage
        self.inputExpression = inputExpression
        print(inputExpression + " is an invalid " + errorMessage)
