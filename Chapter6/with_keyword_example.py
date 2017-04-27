#!/usr/bin/python3


if __name__ == "__main__":
	with open('write_file.txt', 'r+') as file:
		# read the contents of the file and print to the screen
		print(file.read())
		file.write("This is a line appended to the file")

		#rewind the file and read its contents
		file.seek(0)
		print(file.read())
	print("Exited the with keyword code block")

