import machine
from time import sleep
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(sda=machine.Pin(21), scl=machine.Pin(22))

oled = SSD1306_I2C(128, 64, i2c)

def header_text(text):
    LINES_IN = [0,1,2,13,14,15]
    for line in LINES_IN:
        oled.hline(0, line, 128)
    oled.print(text, 0, 7)
    
    
header_text("text")
#oled.hline(0, 15, 128)
i = 2
while True:
    sleep(1)
    oled.print(f'Test - {i}', 0, int(f"{i}0"))
    i = i + 1
    oled.show()
