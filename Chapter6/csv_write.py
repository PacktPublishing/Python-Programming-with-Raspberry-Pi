#!/usr/bin/python3

import csv

if __name__ == "__main__":
	# initialize csv writer
	with open("csv_example.csv", 'w') as csv_file:
		csv_writer = csv.writer(csv_file)

		csv_writer.writerow([123, 456, 789])
		csv_writer.writerow(["Red", "Green", "Blue"])

