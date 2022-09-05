import requests
from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)
app.secret_key = "xxxxxxxxxxxxxxxxxxx"

API_KEY = "15959927002cae2d94c39c62f2266558"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

@app.route("/")
def index():
    welc = ("Enter a city:")
    return render_template("index.html", welc = welc)

@app.route("/outcome")
def weather():
    sliderValue = request.args.get('jsdata')
    day = int(sliderValue) * 8
    city = str(request.args.get('jsdata1')).title()
    
    request_url = f"{BASE_URL}?appid={API_KEY}&lang=en&q={city}"
    response = requests.get(request_url)
    data = response.json() 
        
    if response.status_code == 200:
        
        weather = data['list'][day]['weather'][0]['description'].title()
        temperature = str(round(data['list'][day]['main']['temp'] - 273.15)) + " °C"
        resp = ("[Day " + sliderValue + "] weather in " + city + " is: " + weather + " " + temperature)

    else:
        resp = "I couldn't find that city :( Error: " + str(response.status_code)
        
    return render_template("outcome.html", respp = resp)
  