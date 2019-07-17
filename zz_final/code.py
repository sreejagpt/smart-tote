"""
One of many potential creative solutions for the smart tote - make the LED light up in rainbow
colours in normal light, and green in dim light. The dimmer it is outside, the brighter the light gets.
"""

import board
import analogio
import time
import neopixel_helper

photocell = analogio.AnalogIn(board.A1)
VOLTAGE_IN_NORMAL_LIGHT = 2.85;

def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage

def calculate_brightness(volts):
    return round((1 - (1/VOLTAGE_IN_NORMAL_LIGHT) * volts), 1);

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
