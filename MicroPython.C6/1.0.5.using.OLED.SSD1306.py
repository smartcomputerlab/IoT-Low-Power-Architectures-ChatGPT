from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

def battery_display(sda, scl, battery, duration):
    # Initialize I2C bus
    i2c = I2C(scl=Pin(scl), sda=Pin(sda), freq=400000)
    # Adjust display width/height if different. Common sizes: 128x64 or 128x32.
    # Assuming a 128x64 display:
    width = 128
    height = 64
    # Initialize the OLED display
    oled = SSD1306_I2C(width, height, i2c)
    # Clear the display
    oled.fill(0)
    # Write text to display
    oled.text("Battery readings", 0, 0)
    oled.text("V: {:.2f}".format(battery), 0, 16)
    # Update the display
    oled.show()
    if duration:
        time.sleep(duration)
        oled.poweroff()
        