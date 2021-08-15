"""CAMERA
"""

import picamera


class Camera:
    def __init__(self):
        self.camera = picamera.PiCamera()

    def start_recording(self):
        pass

    def stop_recording(self):
        pass
