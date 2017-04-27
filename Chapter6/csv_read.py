#!/usr/bin/python3

import csv

if __name__ == "__main__":
	# initialize csv writer
	with open("csv_example.csv", 'r') as csv_file:
		csv_reader = csv.reader(csv_file)

		for row in csv_reader:
			print(row)

