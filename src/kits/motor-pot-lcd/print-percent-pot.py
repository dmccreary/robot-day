import machine
from utime import sleep

POT_PIN_1 = 26
MAX_POT_VALUE = 65536 # all 16 bits are on
HALF_MAX = MAX_POT_VALUE
ONE_EIGHT = 3000
ONE_QUARTER = 11000
CENTER_POINT = 17000
THREE_QUARTER = 24000
SEVEN_EIGHTS = 42000

plot_values = ((0,0), (.125, 3000), (.25, 11000), (.5, 17000), (.75, 24000), (.8625, 42000), (1.0, 655360))

adc = machine.ADC(POT_PIN_1)

while True:
    pot_value = adc.read_u16()
    percent_max = round(pot_value/MAX_POT_VALUE * 100, 1)
    print(pot_value, percent_max)
    sleep(.1)
    