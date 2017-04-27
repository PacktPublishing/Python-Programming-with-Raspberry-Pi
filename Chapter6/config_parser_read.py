#!/usr/bin/python3

import configparser

if __name__ == "__main__":
	# initialize ConfigParser
	config_parser = configparser.ConfigParser()

	# Let's read the config file
	config_parser.read('raspi.cfg')

	device_id = config_parser.get('AppInfo', 'id')
	debug_switch = config_parser.get('AppInfo', 'debug_switch')
	sensor_address = config_parser.get('AppInfo', 'sensor_address')

	# execute the code if the debug switch is true
	if debug_switch == "True": 
		print("The device id is " + device_id)
		print("The sensor_address is " + sensor_address)

