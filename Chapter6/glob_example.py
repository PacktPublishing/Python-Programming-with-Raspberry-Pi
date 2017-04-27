#!/usr/bin/python3

import glob

if __name__ == "__main__":
	# List all files
    for file in glob.glob('*.py'):
    	print(file)

    for file in glob.glob('txt_files/file1[0-9][0-9].txt'):
    	print(file)
