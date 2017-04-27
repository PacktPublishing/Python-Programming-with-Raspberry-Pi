#!/usr/bin/python3


if __name__ == "__main__":
	# open text file to read 

	file = open('write_file.txt', 'r')
	
	# read the second line from the file 
	file.seek(53)
	
	data = file.read()
	print(data)
	file.close()