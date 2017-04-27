#!/usr/bin/python3

import random

# create an empty list
random_list = []

for index in range(0,10):
	random_number = random.randint(0, 10)
	random_list.append(random_number)

print("The items in random_list are  ")
print(random_list)

