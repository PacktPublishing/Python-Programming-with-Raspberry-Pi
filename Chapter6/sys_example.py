#!/usr/bin/python3

import sys

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as read_file:
		print(read_file.read())