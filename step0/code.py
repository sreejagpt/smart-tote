"""
Step 0:

Setting up the Gemma M0 microcontroller and blinking the red onboard LED

"""

import board
import digitalio
import time

# Uncomment the line below to start using the onboard LED as output
# led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    # Turn LED on by setting led.value to True below
    # CODE GOES BELOW THIS LINE

    time.sleep(0.5)

    # Turn LED off by setting led.value to False below. This will make the LED blink periodically.
    # CODE GOES BELOW THIS LINE

    time.sleep(0.5)
