import time

import board
import analogio
import neopixel

# Initialize analog input connected to photocell.
photocell = analogio.AnalogIn(board.A1)
DARK_VOLTAGE = 0
DIM_VOLTAGE = 0
BRIGHT_VOLTAGE = 0

# Initialize the output pin on the Gemma M0 that is connected to the NeoPixel
pixel_pin = board.D1

# The number of NeoPixels
num_pixels = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=True)

# Make a function to convert from analog value to voltage.
def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage

# Main loop reads value and voltage every second and prints them out.
while True:
    pixels.fill((0, 0, 0))
    time.sleep(1.0)
    # Read the value, then the voltage.
    val = photocell.value
    volts = analog_voltage(photocell)
    # Print the values:
    print('Photocell value: {0} voltage: {1}V'.format(val, volts))

    if (volts >= DIM_VOLTAGE):
        #Shine neopixel light if getting dim
        pixels.fill((0, 100, 100))
        pixels.show()

    # Delay for a second and repeat!
    time.sleep(1.0)