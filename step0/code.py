"""
Step 0:

Setting up the Gemma M0 microcontroller and turning the red onboard LED on and off

"""

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    #Turn LED on by setting led.value to True below
    time.sleep(0.5)
    #Turn LED on by setting led.value to False below
    time.sleep(0.5)
