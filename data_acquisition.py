import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="environmentvariables.env")

#weather function
API_KEY = os.getenv("WEATHER_API_KEY")
LOCATION = os.getenv("LOCATION")

#Supabase function
#SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
#SUPABASE_URL = os.getenv("SUPABASE_URL")
#SUPABASE_USER_ID = os.getenv("SUPABASE_USER_ID")

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
    
    return data["forecast"]["forecastday"][0]


def get_tube_status():
    #TFL Function
    TFL_URL = "https://api.tfl.gov.uk/line/mode/tube,overground,dlr/status"

    response = requests.get(TFL_URL)
    response.raise_for_status()
    lines = response.json()
    status_messages = []
    for line in lines:
        name = line["name"]
        status = line["lineStatuses"][0]["statusSeverityDescription"]
        status_messages.append(f"{name}: {status}")
    return "\n".join(status_messages)


'''def get_user_location():
    headers = {
        "apikey": SUPABASE_API_KEY,
        "Authorization": f"Bearer {SUPABASE_API_KEY}"
    }
    url = f"{SUPABASE_URL}/rest/v1/user_location?user_id=eq.{SUPABASE_USER_ID}&select=lat,lon&order=updated_at.desc&limit=1"
    res = requests.get(url, headers=headers)
    data = res.json()
    return data[0]["lat"], data[0]["lon"]'''
