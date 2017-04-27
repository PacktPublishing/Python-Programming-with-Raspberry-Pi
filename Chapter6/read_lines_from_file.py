#!/usr/bin/python3


if __name__ == "__main__":
	# open text file to read 
	file = open('read_lines.txt', 'r')

	# read a line from the file 
	data = file.readlines()
	for line in data:
		print(line)

	file.close()