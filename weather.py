import requests
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "ebeebe_ebeebe"

API_KEY = "15959927002cae2d94c39c62f2266558"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

@app.route("/weather")
def index():
    flash("Enter a city name:")
    return render_template("index.html")

@app.route("/outcome", methods=["POST", "GET"])
def weather():
    
    city = str(request.form['name_input']).title()
    request_url = f"{BASE_URL}?appid={API_KEY}&lang=en&q={city}"
    response = requests.get(request_url)
    data = response.json() 
        
    if response.status_code == 200:
            
        sliderValue = request.form['slider_value']
        day = int(sliderValue) * 8
        weather = data['list'][day]['weather'][0]['description'].title()
        temperature = str(round(data['list'][day]['main']['temp'] - 273.15)) + " °C"
        flash("[Day " + sliderValue + "] weather in " + city + " is: " + weather + " " + temperature)

    else:
        error = "I couldn't find that city :( Error: " + str(response.status_code)
        flash(error)
    return render_template("index.html")
    