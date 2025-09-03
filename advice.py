#import googlemaps
import os
from datetime import datetime
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv(dotenv_path="environmentvariables.env")
#GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def wind_chill(temp_c, wind_mph):
    # Only valid for temps <= 10°C and wind >= 3 mph
    temp_f = temp_c * 9/5 + 32
    if wind_mph < 3 or temp_c > 10:
        return temp_c
    chill_f = 35.74 + 0.6215 * temp_f - 35.75 * (wind_mph**0.16) + 0.4275 * temp_f * (wind_mph ** 0.16)
    chill_c = (chill_f - 32) * 5/9
    return chill_c

def generate_advice(forecast: Dict[str, Any]):

    """
    Generate daily clothing and weather advice based on forecast data.

    Parameters
    ----------
    forecast : dict
        Weather forecast dictionary (structured from API response).

    Returns
    -------
    str
        A personalised weather advice message.
    """
    condition = forecast["day"]["condition"]["text"].casefold()
    avg_temp = forecast["day"]["avgtemp_c"]
    chance_of_rain = forecast["day"]["daily_chance_of_rain"]
    max_wind = forecast["day"]["maxwind_mph"]
    evening_temp = forecast["hour"][19]["temp_c"]
    precip = forecast["day"]["totalprecip_mm"]
    max_temp_day = forecast["day"]["maxtemp_c"]

    advice = ["Good morning Neel."]

    # Temperature-based advice
    if avg_temp >= 23:
        advice.append(
            f"It’s gonna be sweaty with an average of {avg_temp}°C "
            f"and a max of {max_temp_day}°C. T-shirts and shorts if possible. "
            f"At 7pm it will be {evening_temp}°C."
        )
    elif avg_temp >= 18:
        advice.append(
            f"Expect mild weather (max {max_temp_day}°C). "
            f"Bring a light jumper as it may get cold later. "
            f"At 7pm it will be {evening_temp}°C."
        )
    elif avg_temp >= 10:
        advice.append(
            f"Could feel chilly depending on the season (max {max_temp_day}°C). "
            f"Definitely take a jacket. At 7pm it will be {evening_temp}°C."
        )
    else:
        advice.append(
            f"Proper cold today (max {max_temp_day}°C). "
            "Layer up with a jacket, hat, and gloves."
        )

    # Rain-based advice
    def rain_message(precip):
        if precip <= 1:
            return "Just a light drizzle — you’ll barely get wet."
        elif precip <= 2:
            return "Light rain in short bursts — raincoat optional."
        elif precip <= 5:
            return "Moderate rain — pack a raincoat or umbrella."
        else:
            return "Steady rain — definitely take a raincoat and umbrella."

    if chance_of_rain >= 50:
        advice.append("Over 50% chance of rain.")
        advice.append(rain_message(precip))
    elif 30 <= chance_of_rain < 50:
        advice.append("Moderate chance of rain.")
        advice.append(rain_message(precip))

    # Condition-based advice
    if "snow" in condition:
        advice.append("Snow is likely — wear boots and warm clothes.")
    elif "sun" in condition:
        advice.append("Sunny skies! Don’t forget sunglasses.")
    elif "thunder" in condition:
        advice.append("Thunderstorms possible - stay safe indoors if needed.")

    return " ".join(advice)




'''def get_top_routes(start_lat, start_lon, end_lat, end_lon, mode="transit", gmaps_key = GOOGLE_MAPS_API_KEY):
    
    gmaps = googlemaps.Client(key=gmaps_key)    

    directions_result = gmaps.directions(
        (start_lat, start_lon),
        (end_lat, end_lon),
        mode=mode,
        departure_time=datetime.now(),
        alternatives=True  
    )

    top_routes = []

    for i, route in enumerate(directions_result[:3]):  # Limit to top 3
        duration = route['legs'][0]['duration']['text']
        steps = route['legs'][0]['steps']
        
        
        summary = []
        for step in steps:
            if 'transit_details' in step:
                line = step['transit_details']['line']['short_name']
                vehicle = step['transit_details']['line']['vehicle']['type']
                stop_from = step['transit_details']['departure_stop']['name']
                stop_to = step['transit_details']['arrival_stop']['name']
                summary.append(f"Take {vehicle} {line} from {stop_from} to {stop_to}")
            else:
                summary.append(step['html_instructions'])

        route_info = {
            "route_number": i + 1,
            "duration": duration,
            "summary": " → ".join(summary)
        }

        top_routes.append(route_info)

    return top_routes'''

