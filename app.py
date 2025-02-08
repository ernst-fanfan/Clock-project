#!/usr/bin/env python3
import requests
from flask import Flask, render_template, Response
import json
import time

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

def get_time_for_timezone(timezone):
    response = requests.get(f"https://timeapi.io/api/time/current/zone?timeZone={timezone}")
    response.raise_for_status()
    return response.json()

@app.route('/', methods=['GET'])
def index():
    timezones = ["America/New_York", "Europe/London", "Asia/Tokyo"]
    times = {tz: get_time_for_timezone(tz) for tz in timezones}
    return render_template('index.html', title="Time", times=times, footer="Created by Ernst Fanfan")

if __name__ == '__main__':
    app.run(debug=True)
