import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="environmentvariables.env")

# Triggering GitHub Action manually


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

TFL_URL = "https://api.tfl.gov.uk/line/mode/tube,overground,dlr/status"

def get_tube_status():
    response = requests.get(TFL_URL)
    response.raise_for_status()
    lines = response.json()
    status_messages = []
    for line in lines:
        name = line["name"]
        status = line["lineStatuses"][0]["statusSeverityDescription"]
        status_messages.append(f"{name}: {status}")
    return "\n".join(status_messages)

