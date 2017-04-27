#!/usr/bin/python3

import requests
import datetime

BIKE_URL = "http://feeds.bayareabikeshare.com/stations/stations.json"
# find your key from ifttt
IFTTT_URL = "https://maker.ifttt.com/trigger/mobile_notify/with/key/$KEY"

if __name__ == "__main__":
  # fetch the bike share information
  response = requests.get(BIKE_URL)
  parsed_data = response.json()
  station_list = parsed_data['stationBeanList']
  for station in station_list:
    if station['id'] == 65 and\
       station['availableBikes'] < 3:
      print("The available bikes is %d" % station['availableBikes'])
      payload = {"value1": station['availableBikes']}
      response = requests.post(IFTTT_URL, json=payload)
      if response.status_code == 200:
        print("Notification successfully triggered")
