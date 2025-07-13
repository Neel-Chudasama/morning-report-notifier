import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="environmentvariables.env")

def send_pushover_notification(message):
    data = {
        "token": os.getenv("PUSHOVER_APP_TOKEN"),
        "user": os.getenv("PUSHOVER_USER_KEY"),
        "message": message
    }
    response = requests.post("https://api.pushover.net/1/messages.json", data=data)
    print("Notification status:", response.status_code)
