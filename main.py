import machine
import network
import time
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

# Initialising the LCD display.
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(19), sda=Pin(23), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('RK', 'rjsk62930')
        while not wlan.isconnected():
            pass
    lcd.putstr('network config:', wlan.ifconfig())

do_connect()

time.sleep(10)
while True:
    lcd.putstr("Hello Szymon")
    sleep(2)
    lcd.clear()
    lcd.putstr("Initialising binary clock")
    sleep(2)
    lcd.clear()
    for i in range(33):
        lcd.putstr(str(bin(i)))
        sleep(1)
        lcd.clear()
