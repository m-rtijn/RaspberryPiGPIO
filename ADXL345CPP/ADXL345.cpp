#include <wriringPiI2C.h>
#include <iostream>

#define POWER_CTL 0x2D

class ADXL345
{
	// Global Variables
	float earthGravityMS2 = 9.80665;
	float scaleMultiplier = 0.0039;
	int address;
	bool DEBUG = false;

    // ADXL345 Registers
    int dataFormat = 0x31;
	int bandwithRate = 0x2C;
	//int POWER_CTL = 0x2D;
	int measure = 0x08;

	int bandwithRate1600HZ = 0x0F;
	int bandwithRate800HZ = 0x0E;
	int bandwithRate400HZ = 0x0D;
	int bandwithRate200HZ = 0x0C;
	int bandwithRate100HZ = 0x0B;
	int bandwithRate50HZ = 0x0A;
	int bandwithRate25HZ = 0x09;

	int range2G = 0x00;
	int range4G = 0x01;
	int range8G = 0x02;
	int range16G = 0x03;

	int DATAX0 = 0x32;

	ADXL345(int inputAddress)
	{
		address = inputAddress;

		wiringPiI2CSetup(address);
	}

	// Enables measurement by writing measre (0x08) to POWER_CTL, register 0x27.
	void EnableMeasurement(void)
	{
		wiringPiI2CWrite(POWER_CTL, measure);
	}

	// Disables measurement by writing 0x00 to POWER_CTL, register 0x27
	void DisableMeasurement()
	{
		// TODO: add this method
		;
	}

	// Reads and returns POWER_CTL, register 0x27
	int ReadMeasurementMode()
	{
		// TODO: add this method
		;
	}

	// Changes the bandwithRate by writing the variable bandwithRate to bandwithRate, register 0x2C
	void SetBandwithRate(int bandwithRate)
	{
		// TODO: add this method
		;
	}

	// Reads bandwithRate, register 0x2C
	int ReadBandwithRate()
	{
		// TODO: add this method
		;
	}

	void SetRange(int range)
	{
		// TODO: add this method
		;
	}

	int ReadRange()
	{
		// TODO: add this method
		;
	}

	float[] GetAllAxes()
	{
		// TODO: add this method
		;
	}

	float GetOneValue()
	{
		// TODO: add this method
		;
	}
};