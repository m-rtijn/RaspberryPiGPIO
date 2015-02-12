This program handles the I2C communication between a Raspberry Pi and a BMP180 Temperature/Pressure sensor
combo, just like my ADXL345 program.

This is still a WIP and only the following methods work and have been tested:

* __init__
* ReadSigned16Bit
* ReadUnsigned16Bit
* ReadCalibrationData
* GetRawTemp
* GetTemp