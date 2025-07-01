#Jeremy Durdel
#Chapter 6 CPX 1
#07/01/2025

from adafruit_circuitplayground import cp
import random
import time

#pattern sets the pattern that the pixels will light up
pattern = [2, 7, 3, 5, 9, 0, 1, 4, 6, 8]
print(pattern)


#pixel_color() picks a random (r, g, b) value
def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_color = (red, green, blue)
    return(random_color)


while True:
    for pixel in pattern:
        time.sleep(.5)
        cp.pixels[pixel] = pixel_color()
        time.sleep(.5)
        cp.pixels[pixel] = (0, 0, 0)
