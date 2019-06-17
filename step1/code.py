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
    neopixel_helper.green();
    print('Photocell voltage: {0}V'.format(volts));
    brightness = calculate_brightness(volts);
    print("Brightness: ", brightness);
    neopixel_helper.set_brightness(brightness);
    time.sleep(1.0);