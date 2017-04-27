#!/usr/bin/python3


if __name__ == "__main__":
	# open text file to read 
	file = open('read_line.txt', 'r')
	# read from file and store it to data
	data = file.read()
	print(data)
	file.close()