#!/usr/bin/python3

import cv2

img = cv2.imread('/home/pi/Desktop/test_shot.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
