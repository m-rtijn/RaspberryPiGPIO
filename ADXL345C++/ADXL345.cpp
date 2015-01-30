#include <wiringPiI2C.h>

class ADXL345
{
	// Global Variables
	const float earthGravityMS2 9.80665;
	const float scaleMultiplier 0.0039;
	int address;
	int fd;
	#define DEBUG false;

    // ADXL345 Registers
	#define dataFormat 0x31;
	#define bandwithRate 0x2C;
	#define POWER_CTL 0x2D;
	#define measure 0x08;

	#define  bandwithRate1600HZ 0x0F;
	#define bandwithRate800HZ 0x0E;
	#define bandwithRate400HZ 0x0D;
	#define bandwithRate200HZ 0x0C;
	#define bandwithRate100HZ 0x0B;
	#define bandwithRate50HZ 0x0A;
	#define bandwithRate25HZ 0x09;

	#define range2G 0x00;
	#define range4G 0x01;
	#define range8G 0x02;
	#define range16G 0x03;

	#define DATAX0 0x32;
	#define DATAX1 0x33;
	#define DATAY0 0x34;
	#define DATAY1 0x35;
	#define DATAZ0 0x36;
	#define DATAZ1 0x37

	ADXL345(int inputAddress)
	{
		address = inputAddress;

		fd = wiringPiI2CSetup(address);
	}

	// Member functions declaration
	void EnableMeasurement(void);
	void DisableMeasurement();
	int ReadMeasurementMode();
	void SetBandwithRate(int rate);
	int ReadBandwithRate();
	void SetRange(int range);
	int ReadRange();
	float[] GetAllAxes();
	float GetOneValue();
};

// Enables measurement by writing measre (0x08) to POWER_CTL, register 0x27.
void ADXL345::EnableMeasurement(void)
{
	wiringPiI2CWriteReg8(fd, POWER_CTL, measure);
}

// Disables measurement by writing 0x00 to POWER_CTL, register 0x27
void ADXL345::DisableMeasurement()
{
	// TODO: add this method
	;
}

// Reads and returns POWER_CTL, register 0x27
int ADXL345::ReadMeasurementMode()
{
	return wiringPiI2CReadReg8(fd, POWER_CTL);
}

// Changes the bandwithRate by writing the variable bandwithRate to bandwithRate, register 0x2C
void ADXL345::SetBandwithRate(int rate)
{
	wiringPiI2CWriteReg8(fd, bandwithRate, rate);
}

// Reads bandwithRate, register 0x2C
int ADXL345::ReadBandwithRate()
{
	return wiringPiI2CReadReg8(fd, bandwithRate) & 0x0F;
}

// Changes the range of the ADXL345
void ADXL345::SetRange(int range)
{
	// TODO: add this method
	;
}

// Reads the range the ADXL345 is set to and returns it.
int ADXL345::ReadRange()
{
	// TODO: add this method
	;
}

// Gets all the axes and returns them in a float array
float[] ADXL345::GetAllAxes()
{
	// First create an array for the raw data
	int rawValues[5] = {};

	// Then read the values from the data registers
	rawValues[0] = wiringPiI2CReadReg8(fd, DATAX0);
	rawValues[1] = wiringPiI2CReadReg8(fd, DATAX1);
	rawValues[2] = wiringPiI2CReadReg8(fd, DATAY0);
	rawValues[3] = wiringPiI2CReadReg8(fd, DATAY1);
	rawValues[4] = wiringPiI2CReadReg8(fd, DATAZ0);
	rawValues[5] = wiringPiI2CReadReg8(fd, DATAZ1);

	// Do the magic bit stuff (I have no clue how bitwise operators work)
	int xInt = rawValues[0] | (rawValues[1] << 8);
	int yInt = rawValues[2] | (rawValues[3] << 8);
	int zInt = rawValues[4] | (rawValues[5] << 8);

	// Multiply the values by the scale multiplier to get the acceleration in g
	float x = xInt * scaleMultiplier;
	float y = yInt * scaleMultiplier;
	float z = zInt * scaleMultiplier;

	// Multiply the values by the gravity in m/s^2 to get the acceleration in m/s^2
	x *= earthGravityMS2;
	y *= earthGravityMS2;
	z *= earthGravityMS2;

	// Create an array for the values
	float finalValues = { x, y, z };

	// Return the values
	return finalValues
}

float ADXL345::GetOneValue()
{
	// TODO: add this method
	;
}