#!/usr/bin/python3

import requests

if __name__ == "__main__":
  # Source for link: http://stackoverflow.com/a/30635751/822170
  try:
    response = requests.get('http://nist.time.gov/actualtime.cgi')
    print(response.text)
  except requests.exceptions.ConnectionError as error:
    print("Something went wrong. Try again")