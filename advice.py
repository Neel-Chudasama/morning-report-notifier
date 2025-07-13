def generate_clothing_advice(weather):
    temp = weather['temp']['day']
    rain = weather.get('rain', 0)
    description = weather['weather'][0]['description']

    if temp < 5:
        advice = "It's freezing ❄️ — wear a coat and gloves."
    elif rain > 0.5:
        advice = "Rain is expected ☔ — take an umbrella."
    elif temp > 20:
        advice = "Hot and sunny 😎 — wear light clothes."
    else:
        advice = "Mild weather 🌤️ — a light jacket will do."

    return f"Today’s forecast: {description}, {temp}°C. {advice}"
