import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="environmentvariables.env")

PUSHOVER_USER_KEY = os.getenv("PUSHOVER_USER_KEY")
PUSHOVER_APP_TOKEN = os.getenv("PUSHOVER_APP_TOKEN")
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def send_weather_notification(message):
    if not PUSHOVER_USER_KEY or not PUSHOVER_APP_TOKEN:
        raise ValueError("Pushover credentials are missing.")

    payload = {
        "token": PUSHOVER_APP_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "message": message,
        "title": "Daily Weather Advice"
    }

    response = requests.post("https://api.pushover.net/1/messages.json", data=payload)

    if response.status_code != 200:
        raise Exception(f"Pushover notification failed: {response.text}")
    
def send_tfl_notification(message):
    data = {
        "token": PUSHOVER_APP_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "message": message,
        "title": "Tube Status Update",
        "priority": 0
    }
    response = requests.post("https://api.pushover.net/1/messages.json", data=data)
    response.raise_for_status()

def send_commute_notification(message):
    data = {
        "token": PUSHOVER_APP_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "message": message,
        "title": "Commute duration Update",
        "priority": 0
    }
    response = requests.post("https://api.pushover.net/1/messages.json", data=data)
    response.raise_for_status()
