#!/usr/bin/python3

from flask import Flask
from gpiozero import OutputDevice

app = Flask(__name__)
lights = OutputDevice(2)

@app.route("/lamp/<control>")
def control(control):
  if control == "on":
    lights.on()
  elif control == "off":
    lights.off()
  return "Table lamp is now %s" % control
  
if __name__ == "__main__":
    app.run('0.0.0.0')