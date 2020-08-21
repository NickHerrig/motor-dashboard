import requests
from pprint import pprint
from datetime import date

from flask import Flask, render_template

app = Flask(__name__)

r = requests.get("https://api.nebullam.com/challengeData")
data = r.json()['data']
date = date.today()

@app.route('/')
def show_dashbaord(data=data):
    return render_template('dashboard.html', data=data, date=date)
