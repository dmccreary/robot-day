# RGB Box

![RGB Box](../img/rgb-box.jpg)

This little box is one of the favorite kits of our staff.
It has a power switch and three potentiometers (pots) hooked
up to a Raspberry Pi Pico.  The pots control the brightness
of the red, green and blue pixels on a low-cost LED strip
of about 10 pixels.  The total part cost is around $11.

## Parts List

1. Raspberry Pi Pico - $4
2. 10-element NeoPixel Strip (WS2811B) - $3
3. Breadboard - $1.50
4. 3 potentiometers - 50 cents each
5. 3 AA battery pack - $1

## Wiring Diagram


## Sample Code

```pyton
# this kit assumes we have three POTs hooked to pins 26, 27 and 28 of the Pico
from machine import ADC, Pin
from utime import sleep
from neopixel import NeoPixel

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 10
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# this is the built-in LED on the Pico which we toggle on and off to show sampling
led = Pin(25, Pin.OUT)

# ADC0 is GPIO 26.  Connect to row 10 the right side
pot1 = ADC(28) # red
pot2 = ADC(27) # green
pot3 = ADC(26) # blue

MAX_DELAY = .5 # seconds

# global variables
delay = .05

# repeat forever
while True:
    # if we have the POTs wired backwards we subtract to get the value
    # read the value from the pot and shift 6 bits
    # The brightness of each LED ranges from 0 to 255 - 8 bits
    pot_value1 = pot1.read_u16() >> 8 
    pot_value2 = pot2.read_u16() >> 8
    pot_value3 = pot3.read_u16() >> 8
    print("rgb", pot_value1, pot_value2, pot_value3)
    
    # update the strip with our new values
    for i in range(NUMBER_PIXELS):
        strip[i] = (pot_value3, pot_value2, pot_value1)
    strip.write()
    
    sleep(delay)
    led.toggle()
```