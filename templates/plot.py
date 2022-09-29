from io import BytesIO
from matplotlib.figure import Figure
import base64
import numpy as np
from datetime import datetime, timedelta

def plot(data, day, change):
    fig = Figure(figsize=(18, 6), dpi=70, facecolor='#292929')
    y = []
    x = []
    for i in range (0,8):
        y.append(round(data['list'][day + i]['main']['temp'] - 273.15))
        now = datetime.now() + timedelta(hours = i * 3)
        current_time = now.strftime("%H:%M")
        x.append(current_time)

    y = [abs(y) for y in y]   
    max_temp = max(y) + 2
   
    ax = fig.subplots()
    ax.set_facecolor("#292929")
    ax.set_xlabel('Hour', color="#F15738")
    ax.set_ylabel('°C', rotation=0, loc="top", color="#F15738")
    ax.spines['bottom'].set_color('#292929')
    ax.spines['top'].set_color('#292929') 
    ax.spines['right'].set_color('#292929')
    ax.spines['left'].set_color('#292929')
    ax.tick_params(axis='x', colors='#F15738')
    ax.tick_params(axis='y', colors='#F15738')
    
    if change == "bar":
        ax.bar(x, y, width=0.7, color="#FBAF40", edgecolor="#F15738", linewidth=3)
        
    else:
        ax.plot(x, y, color="#F15738", linewidth=3)
        ax.fill_between(x,y,color="#FBAF40")

    ax.set(xlim=(-0.5, 7.5), xticks=np.arange(0, 8), ylim=(0, max_temp), yticks=np.arange(0, max_temp, 2))

    buf = BytesIO()
    fig.savefig(buf, format="png")

    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    img = f"<img src='data:image/png;base64,{data}'/>"
    return img