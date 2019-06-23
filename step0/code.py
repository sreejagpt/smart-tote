import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    #Turn LED on by setting led.value to True
    time.sleep(0.5)
    #Turn LED on by setting led.value to False
    time.sleep(0.5)
