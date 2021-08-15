#!/bin/bash

# Update and upgrade
sudo apt update
sudo apt full-upgrade

# Free up space
sudo apt clean

# Install camera stuff
sudo apt install python-opencv python-picamera

# Install the Bluetooth adapter and setup streaming
sudo nano /boot/config.txt
add the line
dtoverlay=pi3-disable-bt

# Install microphone stuff
cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2smic.py
sudo python3 i2smic.py