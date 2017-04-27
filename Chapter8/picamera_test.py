#!/usr/bin/python3

from picamera import PiCamera
from time import sleep 

if __name__ == "__main__":
  with PiCamera() as camera:
    camera.vflip = True
    camera.start_preview()
    sleep(10)
    camera.capture("/home/pi/Desktop/desktop_shot.jpg")
    camera.stop_preview()