#!/usr/bin/python3

import requests

# generate your own API key
APP_ID = '7bf1a7ed318cef61f32bdd193d33fd2b'
ZIP = 94103
URL = """http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}\
&units=imperial""".format(ZIP, APP_ID)

if __name__ == "__main__":
  # API Documentation: http://openweathermap.org/current#current_JSON
  try:
    # encode data payload and post it
    response = requests.get(URL)
    json_data = response.json()
    print("Temperature is %s degrees Fahrenheit" % json_data['main']['temp'])
  except requests.exceptions.ConnectionError as error:
    print("The error is %s" % error)
