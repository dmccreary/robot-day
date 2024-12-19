from machine import Pin, ADC
from utime import sleep
import ssd1306
import config
LED_0 = Pin(0, Pin.OUT)

SCK=Pin(config.SCK_PIN)
SDA=Pin(config.SDA_PIN)
# spi_rx=machine.Pin(4)
spi=machine.SPI(0,baudrate=100000,sck=SCK, mosi=SDA)

CS = Pin(config.CS_PIN)
DC = Pin(config.DC_PIN)
RES = Pin(config.RES_PIN)

oled = ssd1306.SSD1306_SPI(128, 64, spi, DC, RES, CS)
adc = ADC(config.POT_PIN_1)

while True:
    pot_value = adc.read_u16()
    
    oled.fill(0) # erase the entire screen
    oled.text(str(pot_value), 0, 0, 1)
    # Shift value over 9 bits to range from 0 to 127
    width = 127 - (pot_value >> 9)
    oled.text(str(width), 0, 20, 1)
    # draw filled rect at (x=0,y=40) variable width and 20 px high
    oled.fill_rect(0, 40, width, 20, 1)
    oled.show()

    # toogle the LED to show end
    LED_0.toggle()
    sleep(0.05) # 1/20th of a second