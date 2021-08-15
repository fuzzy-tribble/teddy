"""Test the MICROPHONE hardware

Run the install.sh script, 
reboot the machine,
set the duration and card number
test using the following commands
(either in terminal or using the py script here)

Show recording devices and get the card number,
then update the card number ('plughw') in this file
'arecord -l'

python3 microphone.test.py record
(or 'arecord -d 10 - D plughw: 0 - c1 - r 48000 - f S32_LE - t wav - V mono - v outfile.wav')

python3 microphone.test.py playback
(or 'aplay outfile.wav')

"""

import subprocess
import datetime


record_cmd = f'arecord -d {duration} - D plughw: {card_num} - c1 - r 48000 - f S32_LE - t wav - V mono - v {file_name}'
playback_cmd = f'aplay {file_name}'


def setup():
    subprocess.run(["arecord", "-l"])


def record(duration=0, card_num=0, file_name=None):
    if file_name == None:
        file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.wav")
    args = shlex.split(record_cmd)
    subprocess.run(args)


def playback(file_name):
    args = shlex.split(playback_cmd)
    subprocess.run(args)


if __name__ == "__main__":
    setup()     # runs # 'arecord -l' to list devices

    duration = 10    # infinity = 0
    card_num = 0    # 'arecord -l' to list devices and get card number
    file_name = 'test_mic.wav'

    record(duration, file_name=file_name)
    playback(file_name)
