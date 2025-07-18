def wind_chill(temp_c, wind_mph):
    # Only valid for temps <= 10°C and wind >= 3 mph
    temp_f = temp_c * 9/5 + 32
    if wind_mph < 3 or temp_c > 10:
        return temp_c
    chill_f = 35.74 + 0.6215 * temp_f - 35.75 * (wind_mph**0.16) + 0.4275 * temp_f * (wind_mph ** 0.16)
    chill_c = (chill_f - 32) * 5/9
    return chill_c


def generate_advice(forecast):
    condition = forecast["day"]["condition"]["text"]
    avg_temp = forecast["day"]["avgtemp_c"]
    chance_of_rain = forecast["day"]["daily_chance_of_rain"]
    max_wind = forecast["day"]["maxwind_mph"]
    seven_pm_temp = forecast['hour'][19]['temp_c']
    precip = forecast['day']['totalprecip_mm']
    max_temp_day = forecast['day']['maxtemp_c']

    avg_temp = wind_chill(avg_temp,max_wind)

    advice = []

    # Temperature-based advice
    if avg_temp >= 23:
        advice.append("It’s gonna be sweaty the average temperature is going to be 23+ today, with a max temp of " +str(max_temp_day)+". T-shirts and shorts if possible. At 7pm it will hit " + str(seven_pm_temp))
    elif avg_temp >= 18:
        advice.append("Mild weather, with a max temp " +str(max_temp_day)+". Bring a light jumper because it might get cold. At 7pm it will hit " + str(seven_pm_temp))
    elif avg_temp >= 10:
        advice.append("Depending on what the season is this could be quite cold, definitely take a jacket out with you, with a max temp " +str(max_temp_day)+".  At 7pm it will hit " + str(seven_pm_temp))
    else:
        advice.append("It's proper cold man with a max temp of " +str(max_temp_day)+", take a jacket for sure and layer up. Hats and gloves for sure.")

    # Rain-based advice
    if chance_of_rain >= 50:
        advice.append("More than 50 percent chance of rain.")
        if precip > 0 and precip <= 1:
            advice.append("Light drizzle, barely wetting!")
        elif precip > 1 and precip <= 2:
            advice.append("Light rain and short bursts.	Up to you if you want to pack a raincoat.")
        elif precip > 2 and precip <= 5:
            advice.append("Moderate rain, Definitely worth packing a raincoat")
        else:
            advice.append("Steady rain. Definitely take a raincoat and umbrella")
    elif "rain" in condition.lower():
        advice.append("Rain expected. Be prepared!")
        if precip > 0 and precip <= 1:
            advice.append("Light drizzle, barely wetting!")
        elif precip > 1 and precip <= 2:
            advice.append("Light rain and short bursts.	Up to you if you want to pack a raincoat.")
        elif precip > 2 and precip <= 5:
            advice.append("Moderate rain, Definitely worth packing a raincoat")
        else:
            advice.append("Steady rain. Definitely take a raincoat and umbrella")

    # Weather condition-specific
    if "snow" in condition.lower():
        advice.append("Snow is likely — wear boots and warm clothes.")
    elif "sun" in condition.lower():
        advice.append("Sunny skies! Don’t forget sunglasses.")
    elif "thunder" in condition.lower():
        advice.append("Thunderstorms possible — stay safe indoors if needed.")

    return " ".join(advice)
