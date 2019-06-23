import board
import analogio
import time

"""
Step 1

Calibrating our light sensor to the brightness of the room we are in

"""


photocell = analogio.AnalogIn(board.A1);

# Find out what is getting printed out in your serial console and set VOLTAGE_IN_NORMAL_LIGHT to that value below:
VOLTAGE_IN_NORMAL_LIGHT = 999999;

def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage;

while True:
    volts = analog_voltage(photocell);
    print('Voltage in normal light: {0}\n\n'.format(volts));
    time.sleep(1.0);
