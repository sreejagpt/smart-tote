"""
Step 2:

Hook up your sensor input to your NeoPixel light output!

"""

import board
import analogio
import time
import neopixel_helper

photocell = analogio.AnalogIn(board.A1)
# Pop in your voltage value from Step 1 below
VOLTAGE_IN_NORMAL_LIGHT = 9999

def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage

def calculate_brightness(volts):
    return round((1 - (1/VOLTAGE_IN_NORMAL_LIGHT) * volts), 1)

while True:
    # Initially set light to off
    neopixel_helper.off()
    # Read voltage
    current_voltage = analog_voltage(photocell)
    # Calculate brightness on a scale on 0-1 (0.5 is medium brightness)
    brightness = calculate_brightness(current_voltage);
    print('Brightness: {}'.format(brightness));

    """
    Now get creative! Use if statements to wire up brightness values to neopixel functions.

    Eg: if (current_voltage > VOLTAGE_IN_NORMAL_LIGHT):
            neopixel_helper.rainbow()

            OR

        neopixel_helper.set_brightness(brightness)

    """
