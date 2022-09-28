import requests
from flask import Flask, render_template, request
from io import BytesIO
from matplotlib.figure import Figure
import base64
import numpy as np
from datetime import datetime, timedelta

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

        fig = Figure(figsize=(18, 6), dpi=70, facecolor='#292929')
        y = []
        x = []
        for i in range (0,8):
            y.append(round(data['list'][day + i]['main']['temp'] - 273.15))
            now = datetime.now() + timedelta(hours = i * 3)
            current_time = now.strftime("%H:%M")
            x.append(current_time)
            
        max_temp = max(y) + 2
        
        ax = fig.subplots()
        ax.set_facecolor("#292929")
        ax.set_xlabel('Hour', color="#F15738")
        ax.set_ylabel('°C', rotation=0, loc="top", color="#F15738")
        ax.bar(x, y, width=0.7, color="#FBAF40", edgecolor="#F15738", linewidth=3)
        ax.spines['bottom'].set_color('#292929')
        ax.spines['top'].set_color('#292929') 
        ax.spines['right'].set_color('#292929')
        ax.spines['left'].set_color('#292929')
        ax.tick_params(axis='x', colors='#F15738')
        ax.tick_params(axis='y', colors='#F15738')
        ax.set(xlim=(-0.5, 7.5), xticks=np.arange(0, 8), ylim=(0, max_temp), yticks=np.arange(0, max_temp, 2))

        buf = BytesIO()
        fig.savefig(buf, format="png")
        
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        img = f"<img src='data:image/png;base64,{data}'/>"

    else:
        resp = "I couldn't find that city :("
        img = "<p>Error:" + str(response.status_code) + "</p>"
    return render_template("outcome.html", respp = resp, img = img)

if __name__ == "__main__":
    app.run(debug=True)