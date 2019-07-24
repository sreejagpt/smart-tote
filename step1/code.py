import board
import analogio
import time

"""
Step 1

Calibrating our light sensor to the brightness of the room we are in so that
we can tell when it gets brighter or darker relative to the room

"""

photocell = analogio.AnalogIn(board.A2);

"""

A function that calculates the voltage measured across the light sensor.
Dividing by 2**16 - 1 converts a number from an analog value to a voltage reading.

"""
def analog_voltage(adc):
    return adc.value / ((2 ** 16) - 1) * adc.reference_voltage;

while True:
    volts = analog_voltage(photocell);
    print('Voltage in normal light: {0}\n\n'.format(volts));
    time.sleep(1.0);
