#!/usr/bin/env python3
import requests
from flask import Flask, render_template, Response, request, jsonify
import json
import time

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

def get_time_for_timezone(timezone):
    response = requests.get(f"https://timeapi.io/api/time/current/zone?timeZone={timezone}")
    response.raise_for_status()
    return response.json()

def get_all_timezones():
    response = requests.get("https://timeapi.io/api/TimeZone/AvailableTimeZones")
    response.raise_for_status()
    return response.json()

@app.route('/timezones', methods=['GET'])
def timezones():
    timezones = get_all_timezones()
    return jsonify(timezones)

@app.route('/', methods=['GET', 'POST'])
def index():
    all_timezones = get_all_timezones()
    selected_timezones = request.form.getlist('timezones') if request.method == 'POST' else ["America/New_York", "Europe/London", "Asia/Tokyo"]
    times = {tz: get_time_for_timezone(tz) for tz in selected_timezones}
    return render_template('index.html', title="Time", times=times, all_timezones=all_timezones, selected_timezones=selected_timezones, footer="Created by Ernst Fanfan")

if __name__ == '__main__':
    app.run(debug=True)
