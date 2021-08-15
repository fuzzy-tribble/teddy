"""Test LED hardware

Set the led pin, 
run the file, 
make sure the LED turns on and off
"""

import RPi.GPIO as GPIO
import time

led_pin = 18


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(led_pin, GPIO.OUT)


def turn_on():
    print("LED on")
    GPIO.output(led_pin, GPIO.HIGH)


def turn_off():
    print("LED off")
    GPIO.output(led_pin, GPIO.LOW)


def start_blink(n=10):
    for i in range(n):
        turn_on()
        time.sleep(1)
        turn_off()


if __name__ == "__main__":
    setup()
    start_blink(5)
