#!/usr/bin/python3

"""
    Sensor Processing Example
"""
import threading
import time

def sensor_processing(string):
  for num in range(5):
    time.sleep(5)
    print("%s: Iteration: %d" %(string, num))

if __name__ == '__main__':
  thread_1 = threading.Thread(target=sensor_processing, args=("Sensor 1",))
  thread_1.start()

  thread_2 = threading.Thread(target=sensor_processing, args=("Sensor 2",))
  thread_2.start()

  thread_3 = threading.Thread(target=sensor_processing, args=("Sensor 3",))
  thread_3.start()