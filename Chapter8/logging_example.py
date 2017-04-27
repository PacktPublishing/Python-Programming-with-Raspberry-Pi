#!/usr/bin/python3

import requests
import logging

# find your key from ifttt
IFTTT_URL = "https://maker.ifttt.com/trigger/rf_trigger/with/key/$key"

if __name__ == "__main__":
  # fetch the bike share information
  logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', 
                      filename='log_file.log',
                      level=logging.INFO)
  payload = {"value1": "Sample_1", "value2": "Sample_2"}
  response = requests.post(IFTTT_URL, json=payload)
  if response.status_code == 200:
    logging.info("Notification successfully triggered")
  else:
    logging.error("POST request failed")
  