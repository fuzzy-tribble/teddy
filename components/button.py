"""TOGGLE BUTTON
"""

import RPi.GPIO as GPIO

import config.button as conf


class ToggleButton:

    def __init__(self, button_pin):
        GPIO.setwarnings(False)  # Ignore warning for now
        GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering

        # Set button_pin to be an input pin and set initial value to be pulled low (off)
        GPIO.setup(conf.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Setup event on pin 10 rising edge
        GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback)

    def button_callback(channel):
        print("Button was pushed!")

    GPIO.cleanup()  # Clean up
