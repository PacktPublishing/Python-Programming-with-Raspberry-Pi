#!/usr/bin/python3


if __name__ == "__main__":
	# open text file to read 
	file = open('write_file.txt', 'a')
	# read a line from the file 
	file.write('This is a line appended to the file\n')
	file.close()

	file = open('write_file.txt', 'r')
	data = file.read()
	print(data)
	file.close()