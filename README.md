# README

A audio/video journal/recording device for inside a stuffed animal

## Hardware BOM

- Raspberry Pi Zero W PID: 3400
- Adafruit Raspberry Pi Zero Case PID: 3252
- Adafruit I2S MEMS Microphone Breakout - SPH0645LM4H PID: 3421
- Zero Spy Camera for Raspberry Pi Zero PID: 3508
- Standalone Toggle Capacitive Touch Sensor Breakout - AT42QT1012 PID: 1375
  (or any kind of toggle button is fine)

Connectors and stuff

- 0.1" 2x20-pin Strip Right Angle Female Header PID: 2823
- Break-away 0.1" 2x20-pin Strip Dual Male Header PID: 2822
- Through-Hole Resistors - 10K ohm 5% 1/4W - Pack of 25 PID: 2784
- Breadboarding wire bundle PID: 153

(Optional)

- Diffused 3mm LED Pack - 5 LEDs each in 5 Colors - 25 Pack PID: 4202

Note: See the `hw_tests` folder for test scripts to make sure your hardware is connected and working properly

## Software

Clone the git repo then run `install.sh`

Run the script and make sure it works the way you want

Use systemctl to autorun the script on boot

## Enable the camera and SSH remote access.

sudo raspi-config

## Resources

PiCam Docs: https://picamera.readthedocs.io/en/release-1.13/recipes1.html
AudioDocs: https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/raspberry-pi-wiring-test
