"""
Launch point
"""

from components.button import ToggleButton
from components.camera import Camera
from components.microphone import Microphone


button = ToggleButton()
camera = Camera()
mic = Microphone()


def main():
    try:
        while True:
            if button.is_on():
                camera.start_recording()
                mic.start_recording()
            else:
                camera.stop_recording()
                mic.stop_recording()
    finally:
        camera.close_and_clean()
        mic.close_and_clean()


if __name__ == "__main__":
    main()
