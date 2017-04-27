#!/usr/bin/python3
"""
    Personal health improvement example
"""

import fitbit
import datetime

# insert your keys here
CONSUMER_KEY = "KEY"
CONSUMER_SECRET = "KEY"
REFRESH_TOKEN = "KEY"
ACCESS_TOKEN = "KEY"


if __name__ == "__main__":
    fbit_client = fitbit.Fitbit(CONSUMER_KEY,
                                CONSUMER_SECRET,
                                access_token=ACCESS_TOKEN,
                                refresh_token=REFRESH_TOKEN)
    now = datetime.datetime.now()
    end_time = now.strftime("%H:%M")
    response = fbit_client.intraday_time_series('activities/steps',
                                                period='1d')
    print(response['activities-steps'][0]['value'])
