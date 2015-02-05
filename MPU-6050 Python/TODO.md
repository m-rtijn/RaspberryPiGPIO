TODO:
Add:
- Method to get the gyro values
- Methods to change and read the range the accelerometer is set to
- Methods to change and read the range the gyroscope is set to
- In GetAllAccelValues:
	- Options to use the correct scale multiplier for the current range
- Method to disable the temp sensor
- Methods to change the clock source of the device
- Example script
Fix:
- Nothing
Test:
- Everything except for GetAllAccelValues, GetTemp, __init__ and ReadI2CWord