"""

Connect it all together: read the brightness of the room and program your LEDs to light up accordingly

"""

import board
import analogio
import time
import neopixel_helper

photocell = analogio.AnalogIn(board.A1)

# Replace 999999 with your voltage in normal light value from Step1 below
VOLTAGE_IN_NORMAL_LIGHT = 999999;


"""
A function that calculates the voltage measured across the light sensor
"""
def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage
    
"""
A function that takes sensor reading and maps it to a brightness level for the LED. 
If the room is very bright, the output is low (0.1-0.3 range, low brightness)
If the room is very dim, the output brightness is high (0.7-1.9, high brightness)
"""
def calculate_brightness(volts):
    return round((1 - (1/VOLTAGE_IN_NORMAL_LIGHT) * volts), 1);

while True:
    neopixel_helper.off();
    volts = analog_voltage(photocell)
    led_brightness = calculate_brightness(volts);
    
    # Use what you learned in Step2 to program your LEDs based on brightness!
    # You can change colours and brightness based on how bright or dim it is outside.
    # Try it below!

    time.sleep(1.0);
