import tkinter as tk
import requests

API_KEY = "0f94a7b63cb68d2fd36170d6c506b3cc"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather_data():
    city = ent_location.get()
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        display_invalid_label()
        return None
    else:
        hide_invalid_label()
        return response.json()


def display_invalid_label():
    invalid.grid(column=3, row=1)


def hide_invalid_label():
    invalid.grid_forget()


def update_labels(data):
    if data:
        temp = round(data["main"]["temp"])
        humidity = data["main"]["humidity"]
        wind_speed = round(data["wind"]["speed"] * 3.6)
        pressure = data["main"]["pressure"]
        precipitation = round(
            data.get("rain", {"1h": 0}).get("1h", 0) / 10) * 100
    else:
        temp = humidity = wind_speed = pressure = precipitation = ""

    add_temperature.config(text=show_temp(temp))
    add_humidity.config(text=show_humidity(humidity))
    add_wind_speed.config(text=show_wind_speed(wind_speed))
    add_pressure.config(text=show_pressure(pressure))
    add_precipitation.config(text=show_precipitation(precipitation))


def show_temp(temp):
    return f"{temp}°C" if temp else "0"


def show_humidity(humidity):
    return f"{humidity}%" if humidity else "0"


def show_wind_speed(wind_speed):
    return f"{wind_speed} km/h" if wind_speed else "0"


def show_pressure(pressure):
    return f"{pressure} hPa" if pressure else "0"


def show_precipitation(precipitation):
    return f"{precipitation} %" if precipitation else "0"


def search():
    weather_data = get_weather_data()
    update_labels(weather_data)


window = tk.Tk()
window.title("Weather Forecast")
window.geometry("600x600")

frame_labels = tk.Frame(window)
frame_labels.grid(column=0, row=0, sticky="nw")

ent_location = tk.Entry(frame_labels)
ent_location.grid(column=1, row=0)

btn_search = tk.Button(frame_labels, text="Search",
                       command=search, font=("Arial", 12))
btn_search.grid(column=2, row=0, padx=20)

labels_text = ["Temperature:", "Humidity:",
               "Wind Speed:", "Pressure:", "Precipitation:"]
labels = [tk.Label(frame_labels, text=label, font=("Arial", 16))
          for label in labels_text]
for i, lbl in enumerate(labels, start=1):
    lbl.grid(column=0, row=i, padx=20, pady=10, sticky="nw")

add_temperature = tk.Label(frame_labels, font=("Arial", 16), fg="#2D2D2D")
add_temperature.grid(column=1, row=1)

add_humidity = tk.Label(frame_labels, font=("Arial", 16), fg="#2D2D2D")
add_humidity.grid(column=1, row=2)

add_wind_speed = tk.Label(frame_labels, font=("Arial", 16), fg="#2D2D2D")
add_wind_speed.grid(column=1, row=3)

add_pressure = tk.Label(frame_labels, font=("Arial", 16), fg="#2D2D2D")
add_pressure.grid(column=1, row=4)

add_precipitation = tk.Label(frame_labels, font=("Arial", 16), fg="#2D2D2D")
add_precipitation.grid(column=1, row=5)

invalid = tk.Label(frame_labels, text="Invalid Country",
                   font=("Arial", 16), fg="#2D2D2D")

window.mainloop()


"""
Changes made:

- Defined constants for API URL and API Key.
- Split the logic into more descriptive functions.
- Used grid_forget() to hide the "Invalid Country" label instead of destroying and recreating it.
- Simplified label updating by creating a separate function.
- Combined label creation into a loop for cleanliness.
- Added conditional checks in label update functions to handle empty data cases.

This should make the code clearer, more modular, and easier to maintain.
"""