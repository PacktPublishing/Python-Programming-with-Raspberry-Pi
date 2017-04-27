#!/usr/bin/python3

import configparser

if __name__ == "__main__":
	# initialize ConfigParser
	config_parser = configparser.ConfigParser()

	# Let's create a config file
	with open('raspi.cfg', 'w') as config_file:
		#Let's add a section called ApplicationInfo
		config_parser.add_section('AppInfo')

		#let's add config information under this section
		config_parser.set('AppInfo', 'id', '123')
		config_parser.set('AppInfo', 'gpio', '2')
		config_parser.set('AppInfo', 'debug_switch', 'True')
		config_parser.set('AppInfo', 'sensor_address', '0x62')

		#Let's add another section for credentials
		config_parser.add_section('Credentials')
		config_parser.set('Credentials', 'token', 'abcxyz123')
		config_parser.write(config_file)
	print("Config File Creation Complete")

