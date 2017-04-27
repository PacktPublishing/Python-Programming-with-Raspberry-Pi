#!/usr/bin/python3
"""
  Raspberry Pi Zero Motor Control
"""

import time
from Adafruit_MotorHAT import Adafruit_MotorHAT


class Robot(object):
  def __init__(self, left_channel, right_channel):
    self.motor = Adafruit_MotorHAT(0x60)
    self.left_motor = self.motor.getMotor(left_channel)
    self.right_motor = self.motor.getMotor(right_channel)

  def set_speed(self):
    self.left_motor.setSpeed(200)
    self.right_motor.setSpeed(200)

  def stop(self):
    self.left_motor.run(Adafruit_MotorHAT.RELEASE)
    self.right_motor.run(Adafruit_MotorHAT.RELEASE)

  def forward(self, duration):
    self.set_speed()
    self.left_motor.run(Adafruit_MotorHAT.FORWARD)
    self.right_motor.run(Adafruit_MotorHAT.FORWARD)
    time.sleep(duration)
    self.stop()

  def reverse(self, duration):
    self.set_speed()
    self.left_motor.run(Adafruit_MotorHAT.BACKWARD)
    self.right_motor.run(Adafruit_MotorHAT.BACKWARD)
    time.sleep(duration)
    self.stop()

  def left(self, duration):
    self.set_speed()
    self.right_motor.run(Adafruit_MotorHAT.FORWARD)
    time.sleep(duration)
    self.stop()

  def right(self, duration):
    self.set_speed()
    self.left_motor.run(Adafruit_MotorHAT.FORWARD)
    time.sleep(duration)
    self.stop()


if __name__ == "__main__":
  # create an instance  of the robot class with channels 1 and 2
  robot = Robot(1,2)
  print("Moving forward...")
  robot.forward(5)
  print("Moving backward...")
  robot.reverse(5)
  robot.stop()




