"""
One of many potential creative solutions for the smart tote - make the LED light up in rainbow
colours in normal light, and green in dim light. The dimmer it is outside, the brighter the light gets.
"""

import board
import analogio
import time
import neopixel_helper

photocell = analogio.AnalogIn(board.A2)
VOLTAGE_IN_NORMAL_LIGHT = 2.85;

"""

A function that calculates the voltage measured across the light sensor.
Dividing by 2**16 - 1 converts a number from an analog value to a voltage reading.

"""
def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage
    
"""
A function that takes sensor reading and maps it to a brightness level for the LED. 
If the room is very bright, the output is low (0.1-0.3 range, low brightness)
If the room is very dim, the output brightness is high (0.7-1.0 range, high brightness)
In a nutshell - the dimmer the room, the higher the brightness reading.
"""
def calculate_brightness(volts):
    return round((1 - (1/VOLTAGE_IN_NORMAL_LIGHT) * volts), 1) + 0.3;


while True:
    neopixel_helper.off();
    volts = analog_voltage(photocell)
    led_brightness = calculate_brightness(volts);
    
    # Brightness is always inversely proportional to ambient light.
    neopixel_helper.set_brightness(brightness);
    
    if volts < VOLTAGE_IN_NORMAL_LIGHT:
        neopixel_helper.green()
    else:
        neopixel_helper.rainbow()
        
    time.sleep(1.0);
