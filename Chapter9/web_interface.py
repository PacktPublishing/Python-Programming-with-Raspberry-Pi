#!/usr/bin/python3
"""
    Flask framework
"""
from flask import Flask, render_template, request, redirect
from robot import Robot 

app = Flask(__name__)
my_robot = Robot(1,2)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/forward', methods = ['POST'])
def forward():
    my_robot.forward(0.25)
    return redirect('/')

@app.route('/reverse', methods = ['POST'])
def reverse():
    my_robot.reverse(0.25)
    return redirect('/')

@app.route('/left', methods = ['POST'])
def left():
    my_robot.left(0.25)
    return redirect('/')

@app.route('/right', methods = ['POST'])
def right():
    my_robot.right(0.25)
    return redirect('/')

if __name__ == "__main__":
    app.run('0.0.0.0')