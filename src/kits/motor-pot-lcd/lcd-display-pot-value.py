from machine import Pin, PWM, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from time import sleep

POT_PIN_1 = 26
adc = machine.ADC(POT_PIN_1)
SDA_PIN = 16
SCL_PIN = 17

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

counter = 0
while True:
    pot_value = adc.read_u16()
    
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(str(pot_value))
    
    lcd.move_to(0, 1)
    lcd.putstr(str(counter))
    
    sleep(.1)
    counter += 1