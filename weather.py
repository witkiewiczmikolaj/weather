import requests
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "ebeebe_ebeebe"

@app.route("/weather")
def index():
    flash("Enter a city name:")
    return render_template("index.html")

@app.route("/outcome", methods=["POST", "GET"])
def weather():
    flash("Weather in " + str(request.form['name_input']) + "is: ")
    return render_template("index.html")
    
"""
API_KEY = "15959927002cae2d94c39c62f2266558"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&lang=en&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description'].title()
    print(weather)
    temperature = str(round(data['main']['temp'] - 273.15)) + " °C"
    print(temperature)
else:
    print(f"{response.status_code}")
"""