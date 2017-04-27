#!/usr/bin/python3


if __name__ == "__main__":
	# open text file to read 
	file = open('write_file.txt', 'w')
	# read a line from the file 
	file.write('I am excited to learn Python using Raspberry Pi Zero\n')
	file.close()

	file = open('write_file.txt', 'r')
	data = file.read()
	print(data)
	file.close()