import requests
from flask import Flask, render_template, request
from templates.plot import *

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
    sliderValue = request.args.get('day')
    day = int(sliderValue) * 8
    city = str(request.args.get('text')).title()
    change = request.args.get('change')
    
    request_url = f"{BASE_URL}?appid={API_KEY}&lang=en&q={city}"
    response = requests.get(request_url)
    data = response.json() 
    
    if response.status_code == 200:
        
        weather = data['list'][day]['weather'][0]['description'].title()
        temperature = str(round(data['list'][day]['main']['temp'] - 273.15)) + " °C"
        clouds = " Clouds: " + str(data['list'][day]['clouds']['all']) + "%,"
        wind = " Wind: " + str(data['list'][day]['wind']['speed']) + "m/s,"
        humidity = " Humidity: " + str(data['list'][day]['main']['humidity']) + "%"
        icon = "http://openweathermap.org/img/w/" + data['list'][day]['weather'][0]['icon'] + ".png"
        resp = ("<p>[Day " + sliderValue + "] weather in " + city + " is: <img src="+ icon + ">" + weather + " " + temperature + "</p><br><p>" + clouds + wind + humidity + "</p>")
        img = plot(data, day, change)

    else:
        resp = "<p>I couldn't find that city :(</p>"
        img = "<p>Error:" + str(response.status_code) + "</p>"
    return render_template("outcome.html", respp = resp, img = img)

if __name__ == "__main__":
    app.run(debug=True)