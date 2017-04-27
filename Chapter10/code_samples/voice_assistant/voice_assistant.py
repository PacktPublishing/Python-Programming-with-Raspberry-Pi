#!/usr/bin/env python3

import wave
import houndify
import sys
import os
import time
from gpiozero import Button, OutputDevice

CLIENT_ID = "KEY"
CLIENT_KEY = "KEY"

def trigger_function():
  os.system("aplay -D plughw:1,0 /home/pi/beep.wav")
  os.system("arecord -D plughw:2,0 -f S16_LE -d 5 /home/pi/query.wav")
  os.system("aplay -D plughw:1,0 /home/pi/beep.wav")
  call_houndify()

button = Button(4)
light = OutputDevice(3, active_high=False)
button.when_released = trigger_function

def call_houndify():
  # We'll accept WAV files but it should be straightforward to 
  # use samples from a microphone or other source

  BUFFER_SIZE = 512

  client = houndify.StreamingHoundClient(CLIENT_ID, CLIENT_KEY, "test_user")

  ## Pretend we're at SoundHound HQ.  Set other fields as appropriate
  client.setLocation(37.778724, -122.414778)

  fname = "/home/pi/query.wav"

  with wave.open(fname) as audio:
    print("============== %s ===================" % fname)
    audio = wave.open(fname)
    if audio.getsampwidth() != 2:
      print("%s: wrong sample width (must be 16-bit)" % fname)
      sys.exit(0)
    if audio.getframerate() != 8000 and audio.getframerate() != 16000:
      print("%s: unsupported sampling frequency (must be either 8 or 16 khz)" % fname)
      sys.exit(0)
    if audio.getnchannels() != 1:
      print("%s: must be single channel (mono)" % fname)
      sys.exit(0)

    client.setSampleRate(audio.getframerate())
    samples = audio.readframes(BUFFER_SIZE)
    finished = False

    client.start(MyListener())
    while not finished:
      finished = client.fill(samples)
      time.sleep(0.032)     ## simulate real-time so we can see the partial transcripts
      samples = audio.readframes(BUFFER_SIZE)
      if len(samples) == 0:
        break
    client.finish()

#
# Simplest HoundListener; just print out what we receive.
#
# You can use these callbacks to interact with your UI.
#
class MyListener(houndify.HoundListener):

  def onPartialTranscript(self, transcript):
    pass

  def onFinalResponse(self, response):
    if "AllResults" in response:
      result = response["AllResults"][0]
      if result["CommandKind"] == "WeatherCommand":
        os.system("~/speech.sh " + result["SpokenResponseLong"])
      if result['CommandKind'] == "ClientMatchCommand":
        if result["Result"]["action"] == "turn_light_on":
          light.on()
          os.system("~/speech.sh Turning Lights On")
        elif result["Result"]["action"] == "turn_light_off":
          light.off()
          os.system("~/speech.sh Turning Lights Off")
       
  def onError(self, err):
    print("Error: " + str(err))

# The code below will demonstrate how to use streaming audio through Hound
#
if __name__ == '__main__':
  os.system("aplay -D plughw:1,0 /home/pi/beep.wav")
  while True:
    time.sleep(1)
  
