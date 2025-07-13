from apscheduler.schedulers.blocking import BlockingScheduler
from weather import get_weather_data
from advice import generate_clothing_advice
from notifier import send_pushover_notification
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(dotenv_path="environmentvariables.env")

def daily_notification():
    weather = get_weather_data()
    advice = generate_clothing_advice(weather)
    message = f"🌤️ Today's weather: {weather['description']} at {weather['temp']}°C.\n👕 Advice: {advice}"
    send_pushover_notification(message)
    print("Notification sent!")

# Set up scheduler
scheduler = BlockingScheduler()
scheduler.add_job(daily_notification, 'cron', hour=7, minute=0)

print("Scheduler started. Waiting to send daily notifications at 7 AM...")
scheduler.start()
