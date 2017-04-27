#!/usr/bin/python3

import cv2
from picamera import PiCamera
from time import sleep 

if __name__ == "__main__":
  with PiCamera() as camera:
    camera.vflip = True
    camera.start_preview()
    sleep(10)
    camera.capture("/home/pi/Desktop/desktop_shot.jpg")
    camera.stop_preview()

  img = cv2.imread("/home/pi/Desktop/desktop_shot.jpg", cv2.IMREAD_GRAYSCALE)
  cv2.imshow("image", img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()