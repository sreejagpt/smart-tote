import neopixel
import board
import time

DARK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

# Initialize the output pin on the Gemma M0 that is connected to the NeoPixel
pixel_pin = board.D0

# The number of NeoPixels
num_pixels = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=True)

def off():
    pixels.fill(DARK)

def green():
    pixels.fill(GREEN)

def red():
    pixels.fill(RED);

def blue():
    pixels.fill(BLUE);

def rainbow():
    for color in [PURPLE, BLUE, CYAN, GREEN, YELLOW, RED]:
        pixels.fill(color)
        time.sleep(0.5)

def set_brightness(brightness):
    pixels.brightness = brightness;

def _wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
