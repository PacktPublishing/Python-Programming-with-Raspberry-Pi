#!/usr/bin/python3
import subprocess

class TonePlayer(object):
    """A Python class to play boot-up complete tone"""

    def __init__(self, file_name):
        self.file_name = file_name

    def set_volume(self, value):
        """set tone sound volume"""
        subprocess.Popen(["amixer", "set", "'PCM'", str(value)], shell=False)

    def play(self):
        """play the wav file"""
        subprocess.Popen(["aplay", self.file_name], shell=False)


if __name__ == "__main__":
    tone_player = TonePlayer("/home/pi/tone.wav")
    tone_player.set_volume(75)
    tone_player.play()
