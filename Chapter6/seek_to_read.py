#!/usr/bin/python3


if __name__ == "__main__":
	# open text file to read and write
	file = open('write_file.txt', 'r')
	
	# set the pointer to the desired position
	file.seek(5)
	data = file.read(1)
	print(data)
	
	# rewind the pointer 
	file.seek(5)
	data = file.read(7)
	print(data)
	file.close()