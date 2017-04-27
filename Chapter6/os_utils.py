#!/usr/bin/python3

import os
import signal

if __name__ == "__main__":
    # Check if file exists
    if os.path.isfile('/home/pi/Desktop/code_samples/write_file.txt'):
        print('The file exists!')
    else:
        print('The file does not exist!')

    # Confirm code_samples' existence
    if os.path.isdir('/home/pi/Desktop/code_samples'):
        print('The directory exists!')
    else:
        print('The directory does not exist!')

    #remove a file
    os.remove('/home/pi/Desktop/code_samples/read_file.txt')

    # Note: Change the process id to the one that you would like to kill
    try:
        os.kill(1815, signal.SIGKILL)
    except OSError as error:
        print("OS Error " + str(error))