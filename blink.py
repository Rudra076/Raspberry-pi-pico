from machine import Pin
from time import sleep

led = (25, Pin.OUT)

while True:
    led.toggle()
    sleep(0.75)
