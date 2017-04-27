#!/usr/bin/python3
"""
    Flask framework
"""
from flask import Flask, render_template, request, redirect
from gpiozero import OutputDevice

NUM_APPLIANCES = 4

relay_index = [2, 3, 4, 14]
devices = []

for i in range(NUM_APPLIANCES):
        devices.append(OutputDevice(relay_index[i], active_high=False))
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/energize', methods = ['POST'])
def energize():
    if request.form is not None: 
        relays = request.form.getlist("relay")
        for idx in range(0, NUM_APPLIANCES):
            device_name = "relay_" + str(idx)
            if device_name in relays:
                device_state = "state_" + str(idx)
                state = request.form.get(device_state)
                print(state)
                if state == "On":
                    print(state)
                    devices[idx].on()
                elif state == "Off":
                    print(state)
                    devices[idx].off()

    return redirect('/')

if __name__ == "__main__":
    app.run('0.0.0.0')