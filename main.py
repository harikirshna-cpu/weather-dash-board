import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# ---------------- WEATHER FUNCTION WITH CACHE ----------------
weather_cache = {}  # store generated weather per city

def get_weather(city):
    # If city already in cache, return stored weather
    if city in weather_cache:
        return weather_cache[city]

    # Otherwise generate new random weather
    current_weather = {
        "temp": round(random.uniform(15, 35), 1),  # 15°C to 35°C
        "description": random.choice(["clear sky", "cloudy", "rainy", "stormy", "sunny", "foggy"]),
        "wind_speed": round(random.uniform(1, 10), 1)  # 1 to 10 m/s
    }

    # Random forecast (4 future times)
    forecast = []
    times = ["10:00", "13:00", "16:00", "19:00"]
    base_temp = current_weather["temp"]

    for t in times:
        forecast.append({
            "time": t,
            "temp": round(base_temp + random.uniform(-3, 3), 1)  # variation
        })

    # Save in cache
    weather_cache[city] = (current_weather, forecast)
    return current_weather, forecast

# ---------------- FAVORITES FUNCTIONS ----------------
def load_favorites():
    return []

def save_favorites(favorites):
    print("Saved favorites:", favorites)

favorite_cities = load_favorites()

# ---------------- MAIN FUNCTIONS ----------------
def show_weather(city=None):
    """Show weather for entered city or selected favorite."""
    if not city:
        city = city_entry.get()

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name or select one from favorites.")
        return

    current_weather, forecast = get_weather(city)

    # Update label
    weather_label.config(
        text=f"Current Temp: {current_weather['temp']}°C\n"
             f"Description: {current_weather['description']}\n"
             f"Wind Speed: {current_weather['wind_speed']} m/s"
    )

    # Forecast data
    Times = [entry["time"] for entry in forecast]
    Temps = [entry["temp"] for entry in forecast]

    # Clear old chart
    for widget in chart_frame.winfo_children():
        widget.destroy()

    # Create matplotlib figure
    fig = Figure(figsize=(5, 2), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(Times, Temps, marker='o', linestyle='-', color='b')
    ax.set_title(f"Temperature Trend in {city}")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temp °C")
    ax.grid(True)

    # Embed in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def save_favorite():
    city = city_entry.get()
    if city and city not in favorite_cities:
        favorite_cities.append(city)
        favorites_listbox.insert(tk.END, city)
        save_favorites(favorite_cities)

def on_favorite_select(event):
    """Show weather when a favorite is clicked."""
    selection = favorites_listbox.curselection()
    if selection:
        city = favorites_listbox.get(selection[0])
        show_weather(city)

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("600x500")

tk.Label(root, text="Enter City:").pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Show Weather", command=show_weather).pack(pady=5)
tk.Button(root, text="Save Favorite", command=save_favorite).pack(pady=5)

weather_label = tk.Label(root, text="", font=("Arial", 12))
weather_label.pack(pady=10)

chart_frame = tk.Frame(root)
chart_frame.pack(pady=10)

tk.Label(root, text="Favorite Cities:").pack(pady=5)
favorites_listbox = tk.Listbox(root)
favorites_listbox.pack(pady=5)

# Bind click on favorites
favorites_listbox.bind("<<ListboxSelect>>", on_favorite_select)

for city in favorite_cities:
    favorites_listbox.insert(tk.END, city)

root.mainloop()

