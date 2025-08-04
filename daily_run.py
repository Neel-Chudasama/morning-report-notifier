from data_acquisition import get_weather_data, get_tube_status, get_user_location
from advice import generate_advice, get_top_routes
from notifier import send_weather_notification, send_tfl_notification, send_commute_notification # Assuming this function exists

def main():
    forecast = get_weather_data()
    advice = generate_advice(forecast)
    send_weather_notification(advice)

    tube_status = get_tube_status()
    send_tfl_notification(tube_status)

    #start_lat, start_lon = get_user_location()
    #commute_advice = get_top_routes(start_lat, start_lon, end_lat= 51.5145, end_lon= -0.0889)
    #send_commute_notification(commute_advice)


if __name__ == "__main__":
    main()
