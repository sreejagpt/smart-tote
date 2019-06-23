import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# Step 0 blink a red LED on and off
while True:
    #Turn LED on by setting led.value to True below
    time.sleep(0.5)
    #Turn LED on by setting led.value to False below
    time.sleep(0.5)
