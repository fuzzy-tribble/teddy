"""Test TOGGLE BUTTON hardware

Set button_pin variable, 
run script and make sure the value printed on screen is
on or off in accordance with toggling the hw button
"""

from threading import Thread
import RPi.GPIO as GPIO
import time

button_pin = 18


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(button_pin, GPIO.OUT)


def checkloop(self):
    status = False
    while True:
        if GPIO.input(button_pin) == 1:
            if status == False:
                print("on")
                status = True
            else:
                print("off")
                status = False
            while GPIO.input(button_pin) == 1:
                pass


if __name__ == "__main__":
    setup()
    thr = Thread(target=checkloop)
    thr.start()
