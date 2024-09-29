# hass-rest-rpi-gpio
Simple Python REST API to control GPIO powered light (LED) over Raspberry PI from Home Assistant

# Requirements
* Any Raspberry Pi model
* Home Assistant
* Python 3.8+
* Python requests, flask and rpi.gpio modules

# How it works
Wire the device between GPIO 4 (number 7 on BOARD) and any GND.   
In my case it was a Led Fairy Lights battery operated. The 3V GPIO now acts as a battery.

The script runs a web server on port 5000 (default).   
Simply run the script on the Raspberry PI to start the server.

**Home assistant configuration :**
```
switch:
  - platform: rest
    resource: http://<your host or ip address>:5000/light
    name: rpilight
    icon: mdi:lightbulb
    body_on: '{"active": "true"}'
    body_off: '{"active": "false"}'
    is_on_template: "{{ value_json.is_active }}"
    headers:
      Content-Type: application/json
```
  
To test the API from the command line (from the Raspberry PI):   
```
#Get the device status
curl http://localhost:5000/light

#Power up the light
curl http://localhost:5000/light -d '{"active": "true"}' -H 'Content-Type: application/json'

#Power off the light
curl http://localhost:5000/light -d '{"active": "false"}' -H 'Content-Type: application/json'
```
