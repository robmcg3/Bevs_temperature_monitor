"""

uses a dht22 and oled display to show the temperature and humidity. 
oled code heavily based on code posted by A Costas, referenced below

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Raspberry Pi Pico SSD1306 OLED Display (MicroPython)     ┃
┃  https://wokwi.com/projects/359558101922696193$0         ┃
┃                                                          ┃
┃ Copyright (c) 2023 Anderson Costa                        ┃
┃ GitHub: github.com/arcostasi                             ┃
┃ License: MIT                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf, sys
import utime
import dht

pix_res_x = 128
pix_res_y = 64

sensor = dht.DHT22(Pin(0))


def init_i2c(scl_pin, sda_pin):
    # Initialize I2C device
    i2c_dev = I2C(1, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=200000)
    i2c_addr = [hex(ii) for ii in i2c_dev.scan()]
    
    if not i2c_addr:
        print('No I2C Display Found')
        sys.exit()
    else:
        print("I2C Address      : {}".format(i2c_addr[0]))
        print("I2C Configuration: {}".format(i2c_dev))
    
    return i2c_dev

def display_text(oled):
    # Display text on the OLED
    oled.text("Bev's Personal", 5, 5)
    oled.text("Humidity Sensor", 5, 15)
    oled.show()

def display_anima(oled):

    while True:
        
        # Clear the specific line by drawing a filled black rectangle
        oled.fill_rect(45, 35, 60, 35, 1)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        # oled.text(str(hum) + " %" , 45, 50)
        # oled.text(str(temp) + " C", 45, 35)
        
        oled.text( "{:.1f}".format(temp)+ " C", 45, 35)
        oled.text( "{:.1f}".format(hum)+ " %", 45, 50)

        oled.show()
        utime.sleep_ms(1000)

def main():
    i2c_dev = init_i2c(scl_pin=27, sda_pin=26)
    oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)
    display_text(oled)
    display_anima(oled)

if __name__ == '__main__':
    main()
