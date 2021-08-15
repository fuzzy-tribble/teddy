"""Test CAMERA hardware

HARDWARE SPECS
Zero Spy Camera for Raspberry Pi Zero (PRODUCT ID: 3508)
Camera Module Dimensions: 8.6mm x 8.6mm x 5.2mm / .34" x .34" x .2"
Lens Diameter: 6.9mm / .27"
Cable Length (not including module): 52mm / ~2"
Weight: 1.1g

https://picamera.readthedocs.io/en/release-1.13/recipes1.html

"""

import picamera
import datetime
from time import sleep
import subprocess

camera = picamera.PiCamera()


def setup():
    camera.resolution = (1024, 768)
    camera.sharpness = 0
    camera.contrast = 0
    camera.brightness = 50
    camera.saturation = 0
    camera.ISO = 0
    camera.video_stabilization = True
    camera.exposure_compensation = 0
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'average'
    camera.awb_mode = 'auto'
    camera.image_effect = 'none'
    camera.color_effects = None
    camera.rotation = -90
    camera.hflip = False
    camera.vflip = False
    print("Camera setup complete")


def capture_picture(file_name=None):
    if not file_name:
        file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")

    camera.start_preview()
    sleep(2)  # Camera warm-up time
    camera.capture(file_name, use_video_port=True)
    print(file_name+" Taken!")
    # subprocess.Popen(file_name, shell=True)


def capture_timelapse():
    camera.start_preview()
    sleep(2)
    for filename in camera.capture_continuous('img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        sleep(60*5)  # wait 5 minutes


def capture_video(duration=60, file_name=None):
    if not file_name:
        file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")

    camera.resolution = (640, 480)
    camera.start_recording(file_name)
    print("Camera is recording video...")
    camera.wait_recording(duration)
    camera.stop_recording()
    print(f"Camera is done recording video: {file_name}")
    # subprocess.Popen(filename, shell=True)


if __name__ == "__main__":
    try:
        setup()
        capture_picture()
        capture_timelapse()
        capture_video()
    finally:
        camera.close()


# NOTE TO SELF - CHECK OUT OVERLAY FEATURE
# import picamera
# import time

# camera = picamera.PiCamera()
# camera.resolution = (640, 480)
# camera.framerate = 24
# camera.start_preview()
# camera.annotate_text = 'Hello world!'
# time.sleep(2)
# # Take a picture including the annotation
# camera.capture('foo.jpg')
