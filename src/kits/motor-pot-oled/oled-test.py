import machine
import utime
import ssd1306
led = machine.Pin(25, machine.Pin.OUT)

# Black - GND
# Red - 3.2Vold
SCK=machine.Pin(2)
SDA=machine.Pin(3)
# Servo Pins
RES = machine.Pin(12)
DC = machine.Pin(13)
CS = machine.Pin(14)

spi=machine.SPI(0,baudrate=100000,sck=SCK, mosi=SDA)

oled = ssd1306.SSD1306_SPI(128, 64, spi, DC, RES, CS)

# flash all pixels on
oled.fill(1)
oled.show()
utime.sleep(0.5)

oled.fill(0)
oled.text('MicroPython', 0, 0, 1)
oled.text('Rocks!', 20, 20, 1)

oled.show()

# flash the LED to show end
led.high()
utime.sleep(0.5)
led.low()

print('Done')