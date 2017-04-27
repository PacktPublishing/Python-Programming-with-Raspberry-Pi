#!/usr/bin/python3


if __name__ == "__main__":
	# open text file to read and write
	file = open('write_file.txt', 'r+')
	print(file.read())
	
	# set the pointer to the desired position
	file.seek(68)
	file.write('that was modified   ')
	
	# rewind the pointer to the beginning of the file 
	file.seek(0)
	data = file.read()
	print(data)
	file.close()