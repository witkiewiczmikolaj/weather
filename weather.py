import requests
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "ebeebe_ebeebe"

API_KEY = "15959927002cae2d94c39c62f2266558"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/weather")
def index():
    flash("Enter a city name:")
    return render_template("index.html")

@app.route("/outcome", methods=["POST", "GET"])
def weather():
    city = str(request.form['name_input'])
    request_url = f"{BASE_URL}?appid={API_KEY}&lang=en&q={city}"
    response = requests.get(request_url)
    
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description'].title()
        temperature = str(round(data['main']['temp'] - 273.15)) + " °C"
        flash("Weather in " + city + " is: " + weather + " " + temperature)
    else:
        error = "Error: " + str(response.status_code)
        flash(error)
    return render_template("index.html")
