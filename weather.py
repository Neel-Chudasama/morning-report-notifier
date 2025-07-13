import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="environmentvariables.env")


API_KEY = os.getenv("WEATHER_API_KEY")
LAT = os.getenv("LAT")
LON = os.getenv("LON")

def get_weather_data():
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude=minutely,alerts&units=metric&appid={API_KEY}"
    res = requests.get(url)
    data = res.json()
    return data['daily'][0]  # Today’s forecast
