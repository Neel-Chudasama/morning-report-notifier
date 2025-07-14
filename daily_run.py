from weather import get_weather_data
from advice import generate_advice
from notifier import send_notification  # Assuming this function exists

def main():
    forecast = get_weather_data()
    advice = generate_advice(forecast)
    send_notification(advice)

if __name__ == "__main__":
    main()
