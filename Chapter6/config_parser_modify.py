#!/usr/bin/python3

import configparser

if __name__ == "__main__":
	# initialize ConfigParser
	config_parser = configparser.ConfigParser()

	# Let's read the config file
	config_parser.read('raspi.cfg')

	# Set firmware version
	config_parser.set('AppInfo', 'fw_version', 'A3')

	# write the updated config to the config file
	with open('raspi.cfg', 'w') as config_file:
		config_parser.write(config_file)

