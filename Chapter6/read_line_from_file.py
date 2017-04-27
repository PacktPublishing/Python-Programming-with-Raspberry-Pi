#!/usr/bin/python3


if __name__ == "__main__":
	# open text file to read 
	file = open('read_line.txt', 'r')

	# read a line from the file 
	data = file.readline()
	print(data)

	# read another line from the file
	data = file.readline()
	print(data)

	file.close()