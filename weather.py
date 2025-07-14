import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="environmentvariables.env")

API_KEY = os.getenv("WEATHER_API_KEY")
LOCATION = os.getenv("LOCATION")

def get_weather_data():
    url = f"http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": API_KEY,
        "q": LOCATION,
        "days": 1,
        "aqi": "no",
        "alerts": "no"
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # Return the first forecast day (today)
    return data["forecast"]["forecastday"][0]

