#!/usr/bin/env python3
import requests
import redis
import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

@app.route('/', methods=['GET', 'POST'])
def index():
    # app.logger.debug("| index()")
    response = requests.get("https://timeapi.io/api/time/current/zone?timeZone=Europe%2FAmsterdam")
    response.raise_for_status()
    data = response.json()

    return  render_template('index.html', **{
                "title": "Time",
                "location": data.get('timeZone'),
                "time": data.get('time'),
                "button": "Check time",
                "footer": "Created by Ernst Fanfan",
            })

if __name__ == '__main__':
    app.run(debug=True)
