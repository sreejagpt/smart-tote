import time
import board
import analogio
import neopixel_helper


# Initialize analog input connected to photocell.
photocell = analogio.AnalogIn(board.A1)
DARK_VOLTAGE = 0
DIM_VOLTAGE = 0
BRIGHT_VOLTAGE = 0

# Make a function to convert from analog value to voltage.
def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage

# Main loop reads value and voltage every second and prints them out.
while True:
    neopixel_helper.off()
    time.sleep(1.0)
    # Read the value, then the voltage.
    val = photocell.value
    volts = analog_voltage(photocell)
    # Print the values:
    print('Photocell value: {0} voltage: {1}V'.format(val, volts))
    if (volts >= DIM_VOLTAGE):
        #Shine neopixel light if getting dim
        neopixel_helper.green()
        time.sleep(1.0)
        neopixel_helper.increase_brightness()
        time.sleep(1.0)
        neopixel_helper.decrease_brightness()



    # Delay for a second and repeat!
    time.sleep(1.0)