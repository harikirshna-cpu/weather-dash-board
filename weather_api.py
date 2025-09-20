
import requests
from tkinter import messagebox

API_KEY = "a472bf03dac35ce7a3bb17bd5ea165a3"  

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != "200":
            messagebox.showerror("Error", f"City not found: {city}")
            return None

        current = data["list"][0]
        current_weather = {
            "temp": current["main"]["temp"],
            "description": current["weather"][0]["description"],
            "wind_speed": current["wind"]["speed"],
            
            
        }

        forecast = [(item["dt_txt"], item["main"]["temp"]) for item in data["list"][:8]]
        return current_weather, forecast
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None