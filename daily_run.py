from weather import get_weather_data
from advice import generate_clothing_advice
from notifier import send_pushover_notification
from dotenv import load_dotenv

load_dotenv(dotenv_path="environmentvariables.env")

def main():
    weather = get_weather_data()
    advice = generate_clothing_advice(weather)
    message = f"🌤️ Today's weather: {weather['description']} at {weather['temp']}°C.\n👕 Advice: {advice}"
    send_pushover_notification(message)

if __name__ == "__main__":
    main()
