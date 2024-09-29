#!/usr/bin/env python3

from flask import Flask, request, json, jsonify
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED = 7 #Define GPIO Port used
GPIO.setup(LED, GPIO.OUT)

api = Flask(__name__)

@api.route('/light', methods=['GET'])
def get_light():
  state = GPIO.input(LED)
  if state :
    return jsonify({"is_active": "true"})
  else :
    return jsonify({"is_active": "false"})

@api.route('/light', methods=['POST'])
def post_light():
  data = request.json
  active = data.get('active')
  if active == "true":
    GPIO.output(LED, GPIO.HIGH)
  else:
    GPIO.output(LED, GPIO.LOW)
  state = GPIO.input(LED)
  if state :
    return jsonify({"is_active": "true"})
  else :
    return jsonify({"is_active": "false"})

if __name__ == '__main__':
    api.run(host='0.0.0.0')
