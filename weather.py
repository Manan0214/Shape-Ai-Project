import requests as r
import datetime as dt

api_key = "0b530067c36ff1b4c6b44057e2164f6b"

location = str(input("Enter your location: "))

data = r.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}")
json_data = data.json()

# TEMPERATURE VARIABLES
temp = f"{int(json_data['main']['temp'] - 273)}°C"
max_temp = f"{int(json_data['main']['temp_max'] - 273)}°C"
min_temp = f"{int(json_data['main']['temp_min'] - 273)}°C"

# CONDTIONS
condition = json_data['weather'][0]['main']
wind_speed = f"{int(json_data['wind']['speed'])} Km/h"
humidity = f"{int(json_data['main']['humidity'])}%"

time = dt.datetime.now().strftime("%d %b | %I:%M %p")

with open("Weather-report.txt", "a") as f:
    print("Weather Stats for - {}  | {}".format(location.title(), time))
    print("-------------------------------------------------------------")
    print(f"Current Temperature: {temp}\nMaximum\Miminum Temperature: {max_temp}\\{min_temp}")
    print(f"Humidity: {humidity}\t Conditions: {condition}\nWind Speed: {wind_speed}")
    print("-----------------------**********-------------------------\n\n")


    f.write(f"Weather Stats for - {location.title()}  | {time}\n")
    f.write("-------------------------------------------------------------\n")
    f.write("Current Temperature: {temp}\nMaximum\Miminum Temperature: {max_temp}\\{min_temp}\n")
    f.write("Humidity: {humidity}\t Conditions: {condition}\nWind Speed: {wind_speed}\n")
    f.write("-----------------------**********-------------------------\n\n\n")
