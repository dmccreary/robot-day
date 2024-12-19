from machine import Pin
import utime
import ssd1306
import config
led = machine.Pin(25, machine.Pin.OUT)

SCK=Pin(config.SCK_PIN)
SDA=Pin(config.SDA_PIN)
# spi_rx=machine.Pin(4)
spi=machine.SPI(0,baudrate=100000,sck=SCK, mosi=SDA)

CS = Pin(config.CS_PIN)
DC = Pin(config.DC_PIN)
RES = Pin(config.RES_PIN)

oled = ssd1306.SSD1306_SPI(128, 64, spi, DC, RES, CS)

# flash all pixels on
oled.fill(1)
oled.show()
utime.sleep(0.5)

oled.fill(0)
oled.text('MicroPyton', 0, 0, 1)
oled.text(' Rocks!', 20, 20, 1)

oled.show()

# flash the LED to show end
led.high()
utime.sleep(0.5)
led.low()

print('Done')