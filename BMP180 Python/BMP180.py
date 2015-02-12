# This program handles the communication over I2C
# between a Raspberry Pi and a BMP180 Temperature/Pressure sensor
# Made by: MrTijn/Tijndagamer
# Copyright 2015

import smbus
import math
from time import sleep

class BMP180:
    # Global variables
    address = None
    bus = smbus.SMBus(1)
    mode = 1 # TODO: Add a way to change the mode

    # BMP180 registers
    controlReg = 0xF4
    dataReg = 0xF6

    # Calibration data registers
    calAC1Reg = 0xAA
    calAC2Reg = 0xAC
    calAC3Reg = 0xAE
    calAC4Reg = 0xB0
    calAC5Reg = 0xB2
    calAC6Reg = 0xB4
    calB1Reg = 0xB6
    calB2Reg = 0xB8
    calMBReg = 0xBA
    calMCReg = 0xBC
    calMDReg = 0xBE

    # Calibration data variables
    calAC1 = 0
    calAC2 = 0
    calAC3 = 0
    calAC4 = 0
    calAC5 = 0
    calAC6 = 0
    calB1 = 0
    calB2 = 0
    calMB = 0
    calMC = 0
    calMD = 0


    def __init__(self, address):
        self.address = address
        
        # Get the calibration data from the BMP180
        ReadCalibrationData()

    # I2C methods

    # Reads a 16-bit signed value from the given register and returns it
    def ReadSigned16Bit(self, register):
        # Read the raw values from the registers
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)

        if high > 127:
            high -= 256
        
        return (high << 8) + low

    # Reads a 16-bit unsigned value from the given register and returns it
    def ReadUnsigned16Bit(self, register):
        # Read the raw values from the registers
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)

        return (high << 8) + low

    # BMP180 interaction methods

    # Reads and stores the raw calibration data
    def ReadCalibrationData(self):
        self.calAC1 = self.ReadSigned16Bit(self.calAC1Reg)
        self.calAC2 = self.ReadSigned16Bit(self.calAC2Reg)
        self.calAC3 = self.ReadSigned16Bit(self.calAC3Reg)
        self.calAC4 = self.ReadUnsigned16Bit(self.calAC4Reg)
        self.calAC5 = self.ReadUnsigned16Bit(self.calAC5Reg)
        self.calAC6 = self.ReadUnsigned16Bit(self.calAC6Reg)
        self.calB1 = self.ReadSigned16Bit(self.calB1Reg)
        self.calB2 = self.ReadSigned16Bit(self.calB2Reg)
        self.calMB = self.ReadSigned16Bit(self.calMBReg)
        self.calMC = self.ReadSigned16Bit(self.calMCReg)
        self.calMD = self.ReadSigned16Bit(self.calMDReg)

    # Reads and returns the raw temperature data
    def GetRawTemp(self):
        # Write 0x2E to controlReg, 0xF4, to start the measurement
        self.bus.write_byte_data(self.address, controlReg, 0x2E)

        # Wait 4,5 ms
        sleep(0.0045)

        # Read the raw data from the dataReg, 0xF6
        rawData = ReadUnsigned16Bit(self.dataReg)

        # Return the raw data
        return rawData

    # Reads and returns the raw pressure data
    def GetRawPressure(self):
        # Write 0x43 + (self.mode << 6) to the controlReg, 0xF4, to start the measurement
        self.bus.write_byte_data(self.address, controlReg, 0x34 + (self.mode << 6))

        # Sleep for 8 ms.
        # TODO: Way to use the correct wait time for the current mode
        sleep(0.008)

        # Read the raw data from the dataReg, 0xF6
        MSB = self.bus.read_byte_data(self.address, dataReg)
        LSB = self.bus.read_byte_data(self.address, dataReg + 1)
        XLSB = self.bus.read_byte_data(self.address, dataReg + 2)

        rawData = ((MSB << 16) + (LSB << 8) + XLSB) >> (8 - self.mode)

        return rawData
        

    # Reads and returns the actual temperature
    def GetTemp(self):
        rawTemp = self.GetRawTemp()

        X1 = 0
        X2 = 0
        B5 = 0
        actualTemp = 0.0

        X1 = ((rawTemp - self.calAC6) * self.calAC5) / math.pow(2, 15)
        X2 = (calMC * math.pow(2, 11)) / (X1 + self.calMD)
        B5 = X1 + X2
        actualTemp = ((B5 + 8) / math.pow(2, 4)) / 10

        return actualTemp

    def GetPressure(self):
        pass

    def GetAltitude(self):
        pass
