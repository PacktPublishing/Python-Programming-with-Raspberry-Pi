#!/usr/bin/env python3

import wave
import houndify
import sys
import os
import time
from gpiozero import OutputDevice

CLIENT_ID = "KEY"
CLIENT_KEY = "KEY"

#
# Simplest HoundListener; just print out what we receive.
#
# You can use these callbacks to interact with your UI.
#
class MyListener(houndify.HoundListener):

  def __init__(self):
    self.light = OutputDevice(3)

  def onPartialTranscript(self, transcript):
    pass

  def onFinalResponse(self, response):
    if "AllResults" in response:
      result = response["AllResults"][0]
      if result['CommandKind'] == "ClientMatchCommand":
        if result["Result"]["action"] == "turn_light_on":
          self.light.on()
          os.system("~/speech.sh Turning Lights On")
          print("Lights On")
        elif result["Result"]["action"] == "turn_light_off":
          self.light.off()
          os.system("~/speech.sh Turning Lights Off")
       
  def onError(self, err):
    print("Error: " + str(err))

# The code below will demonstrate how to use streaming audio through Hound
#
if __name__ == '__main__':
  # We'll accept WAV files but it should be straightforward to 
  # use samples from a microphone or other source

  BUFFER_SIZE = 512

  if len(sys.argv) < 2:
    print("Usage: %s <client ID> <client key> <wav file> [ <more wav files> ]" % sys.argv[0])
    sys.exit(0)

  client = houndify.StreamingHoundClient(CLIENT_ID, CLIENT_KEY, "test_user")

  ## Pretend we're at SoundHound HQ.  Set other fields as appropriate
  client.setLocation(37.778724, -122.414778)


  for fname in sys.argv[1:]:
    print("============== %s ===================" % fname)
    audio = wave.open(fname)
    if audio.getsampwidth() != 2:
      print("%s: wrong sample width (must be 16-bit)" % fname)
      break
    if audio.getframerate() != 8000 and audio.getframerate() != 16000:
      print("%s: unsupported sampling frequency (must be either 8 or 16 khz)" % fname)
      break
    if audio.getnchannels() != 1:
      print("%s: must be single channel (mono)" % fname)
      break

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
