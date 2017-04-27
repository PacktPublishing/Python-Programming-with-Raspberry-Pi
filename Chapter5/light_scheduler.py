#!/usr/bin/python3
import schedule
import time
from gpiozero import OutputDevice

class LightScheduler(object):
    """A Python class to turn on/off lights"""

    def __init__(self, start_time, stop_time):
        self.start_time = start_time
        self.stop_time = stop_time
        # lamp is connected to GPIO pin2. 
        self.lights = OutputDevice(2)

    def init_schedule(self):
        # set the schedule
        schedule.every().day.at(self.start_time).do(self.on)
        schedule.every().day.at(self.stop_time).do(self.off)

    def on(self):
        """turn on lights"""
        self.lights.on()

    def off(self):
        """turn off lights"""
        self.lights.off()


if __name__ == "__main__":
    lamp = LightScheduler("18:30", "9:30")
    lamp.on()
    time.sleep(50)
    lamp.off()
    lamp.init_schedule()
    while True: 
        schedule.run_pending()
        time.sleep(1)
