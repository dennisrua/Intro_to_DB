import requests
import os
import json
# cwd = os.getcwd()
API_KEY = "6235d180617c73fd58a4e4f889f1eb0b"
CITY = input("Enter city location: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

res = requests.get(url)

weather_data = res.json()

print(f"weather data as follows: \n Temperature : {weather_data['main']['temp']}°C ") 

print(json.dumps(weather_data, indent = 4))
# print(cwd)
