# # our program
# # Text input field (location) - search button
# # 6 Labels (Location, Temperature, Humidity, Wind Speed, Pressure, Precipitation)


import tkinter as tk
# # import tkinter.ttk as ttk
import requests


def getWeatherData():
    # Genterate data with api key from openweathermap.org
    city = ent_location.get()
    api_key = "0f94a7b63cb68d2fd36170d6c506b3cc"
    complete_url = f"https://api.openweathermap.org/data/2.5/weather?q={
        city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)

    invalid = tk.Label(frame_labels, text="City Not Found!",
                       font=("Arial", 16), fg="#2D2D2D")
    if response.status_code != 200:
        invalid.grid(column=3, row=1)
        return
    else:
        invalid.destroy()
    weather_data = response.json()

    temp = round(weather_data["main"]["temp"])
    humidity = weather_data["main"]["humidity"]
    wind_speed = round(weather_data["wind"]["speed"] * 3.6)
    pressure = weather_data["main"]["pressure"]
    if "rain" in weather_data:
        precipitation = round(weather_data["rain"].get(
            "1h", 0) / 10) * 100  # Multiply by 100 for millimeters
    else:
        precipitation = 0  # If rain data is not available, set precipitation to 0

    return temp, humidity, wind_speed, pressure, precipitation


# Function to change all labels when user clicked the button
def search():
    # update = lbl_temperature.cget("text") + " Testing"
    # lbl_temperature.config(text=update)
    temp, humidity, wind_speed, pressure, precipitation = getWeatherData()

    add_temperature = tk.Label(frame_labels, text=showTemp(
        temp), font=("Arial", 16), fg="#2D2D2D")
    add_temperature.grid(column=1, row=1)
    add_humidity = tk.Label(frame_labels, text=showHumidity(
        humidity), font=("Arial", 16), fg="#2D2D2D")
    add_humidity.grid(column=1, row=2)
    add_wind_speed = tk.Label(frame_labels, text=showWindSpeed(
        wind_speed), font=("Arial", 16), fg="#2D2D2D")
    add_wind_speed.grid(column=1, row=3)
    add_pressure = tk.Label(frame_labels, text=showPressure(
        pressure), font=("Arial", 16), fg="#2D2D2D")
    add_pressure.grid(column=1, row=4)
    add_precipitation = tk.Label(frame_labels, text=showPrecipitation(
        precipitation), font=("Arial", 16), fg="#2D2D2D")
    add_precipitation.grid(column=1, row=5)


def showTemp(temp):
    return f"{temp}°C"


def showHumidity(humidity):
    return f"{humidity}%"


def showWindSpeed(wind_speed):
    return f"{wind_speed} km/h"


def showPressure(pressure):
    return f"{pressure} hPa"


def showPrecipitation(precipitation):
    return f"{precipitation} %"


window = tk.Tk()
window.title("Weather Forecast")
window.geometry("600x400")


# Frame to group all 6 Labels
frame_labels = tk.Frame(window)
frame_labels.grid(column=0, row=0, sticky="nw")


ent_location = tk.Entry(frame_labels)
ent_location.grid(column=1, row=0)

btn_search = tk.Button(frame_labels, text="Search",
                       command=search, font=("Arial", 12))
btn_search.grid(column=2, row=0, padx=20)


lbl_location = tk.Label(frame_labels, text="Location: ",
                        font=("Arial", 20, "bold"))
lbl_temperature = tk.Label(
    frame_labels, text="Temperature: ", font=("Arial", 16))
lbl_humidity = tk.Label(frame_labels, text="Humidity: ", font=("Arial", 16))
lbl_wind_speed = tk.Label(
    frame_labels, text="Wind Speed: ", font=("Arial", 16))
lbl_pressure = tk.Label(frame_labels, text="Pressure: ", font=("Arial", 16))
lbl_precipitation = tk.Label(
    frame_labels, text="Precipitation: ", font=("Arial", 16))

# lbl_location.place(relx=0.5, rely=0.1, anchor="center")
lbl_location.grid(column=0, row=0, padx=20, pady=10, sticky="nw")
lbl_temperature.grid(column=0, row=1, padx=20, pady=10, sticky="nw")
lbl_humidity.grid(column=0, row=2, padx=20, pady=15, sticky="nw")
lbl_wind_speed.grid(column=0, row=3, padx=20, pady=15, sticky="nw")
lbl_pressure.grid(column=0, row=4, padx=20, pady=15, sticky="nw")
lbl_precipitation.grid(column=0, row=5, padx=20, pady=15, sticky="nw")


window.mainloop()
