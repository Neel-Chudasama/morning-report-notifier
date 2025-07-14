def generate_advice(forecast):
    condition = forecast["day"]["condition"]["text"]
    avg_temp = forecast["day"]["avgtemp_c"]
    chance_of_rain = forecast["day"]["daily_chance_of_rain"]

    advice = []

    # Temperature-based advice
    if avg_temp >= 25:
        advice.append("It’s hot today. Wear light clothing.")
    elif avg_temp >= 18:
        advice.append("Mild weather. A T-shirt or light jumper is fine.")
    elif avg_temp >= 10:
        advice.append("A bit chilly. Wear a jacket.")
    else:
        advice.append("Cold weather — bundle up with a coat.")

    # Rain-based advice
    if chance_of_rain >= 50:
        advice.append("There's a good chance of rain. Bring an umbrella!")
    elif "rain" in condition.lower():
        advice.append("Rain expected. Be prepared!")

    # Weather condition-specific
    if "snow" in condition.lower():
        advice.append("Snow is likely — wear boots and warm clothes.")
    elif "sun" in condition.lower():
        advice.append("Sunny skies! Don’t forget sunglasses.")
    elif "thunder" in condition.lower():
        advice.append("Thunderstorms possible — stay safe indoors if needed.")

    return " ".join(advice)
