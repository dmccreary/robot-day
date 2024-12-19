from machine import Pin, ADC, PWM
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

# MAX ADC value is 2^16 0 = 65536
# 3700 just barely moves a DC motor sometimes
MAX_POWER_LEVEL = 65536
DEMO_POWER_LEVEL = 20000
# lower right pins with USB on top
FORWARD_PIN = config.MOTOR_FORWARD_PIN
REVERSE_PIN = config.MOTOR_REVERSE_PIN

forward = PWM(Pin(FORWARD_PIN))
forward.freq(1000)
reverse = PWM(Pin(REVERSE_PIN))
reverse.freq(1000)
# turn off reverse
reverse.duty_u16(0)

def main():
    while True:
        pot_value = adc.read_u16()
        # scale percent from 0.00 to 1.00
        percent =  1 - (pot_value / 65536)
        
        oled.fill(0) # erase the entire screen
        oled.text(str(pot_value), 0, 0, 1)
        # Shift value over 9 bits to range from 0 to 127
        width = 127 - (pot_value >> 9)
        oled.text(str(width), 0, 10, 1)
        oled.text(str(round(percent*100, 2)), 0, 20, 1)
        # draw filled rect at (x=0,y=40) variable width and 20 px high
        oled.fill_rect(0, 40, width, 20, 1)
        oled.show()
        
        # forward.duty_u16(65025 - pot_value//16)
        forward.duty_u16(int(DEMO_POWER_LEVEL*percent))
        # toogle the LED to show end
        # LED_0.toggle()
        sleep(0.05) # 1/20th of a second

try:
    main()
except KeyboardInterrupt:
    print('Got ctrl-c')
finally:
    # Optional cleanup code
    print('Cleaning up')
    print('Powering down all motors now.')
    forward.duty_u16(0)
    reverse.duty_u16(0)