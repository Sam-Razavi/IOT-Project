# Import libraries
from machine import Pin  # import Pin definitions
import time  # import timer library
import boot  # import boot.py to check WiFi connection

# define GP16 as output pin
redLED = Pin(16, Pin.OUT)

# start loop
while True:
    if boot.wifi_connected:  # check if connected to WiFi
        redLED.on()  # turn on red LED
        time.sleep(0.3)  # wait 0.3 seconds
        redLED.off()  # turn off red LED
        time.sleep(0.8)  # wait 0.8 second
    else:
        redLED.off()  # Ensure LED is off if not connected
        print("Not connected to WiFi")
        time.sleep(1)  # wait 1 second before checking again
