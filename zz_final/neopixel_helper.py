import neopixel
import board

# Initialize the output pin on the Gemma M0 that is connected to the NeoPixel
pixel_pin = board.D1

# The number of NeoPixels
num_pixels = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=True)

def off():
    pixels.fill((0,0,0))

def green():
    pixels.fill((0, 255, 0))

def red():
    pixels.fill((255, 0, 0))

def blue():
    pixels.fill((0, 0, 255))

def increase_brightness():
    currentBrightness = pixels.brightness;
    pixels.brightness = currentBrightness * 2

def decrease_brightness():
    currentBrightness = pixels.brightness;
    pixels.brightness = currentBrightness / 2