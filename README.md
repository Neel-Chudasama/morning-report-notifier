# Morning Report 

This is a personal automation project that sends a **daily morning report** to my phone with:

- 🌡️ The day's weather forecast (from [WeatherAPI.com](https://www.weatherapi.com/))
- 👕 Clothing advice based on the temperature and weather conditions
- 🚇 Live status updates for all London Underground (TfL) tube lines (from [api.tfl.gov.uk](https://api.tfl.gov.uk/))
- 🧭 Personalized commute time and suggested travel routes using your phone’s real-time location (via iOS Shortcuts + Supabase) and Google Maps Routes API (from [googlemapsapi.com](https://developers.google.com/maps/documentation/routes))

The report is delivered to my phone every morning at 7:00 AM using Pushover.

---

## Features

- Fetches **daily weather data** for London using WeatherAPI
- Generates smart **clothing advice** (e.g. *"Take a jacket, it might rain!"*)
- Connects to **TfL API** to check live status of all tube lines
- Uses my **live phone location** and send data to Supabase table
- **Extracts** data from Supabase table and calculates commute time
- Suggests **top 3 route** options from Google Maps API (via transit)
- Sends the combined report to your **Pushover app** on mobile

---

## Project Structure

```
weather-notifier/
│
├── 🌤️ data_acquisition.py         # Weather + TfL + Supabase + Commute route fetch
├── 👔 advice.py                   # AI-driven clothing recommendation engine, commute time calculation - Google Maps API integration
├── 📱 notifier.py                 # Multi-channel notification dispatcher
├── ⚡ daily_run.py                # Automated pipeline executor
├── 📦 requirements.txt            # Dependency management
├── 🔧 .github/workflows/
│   └── ⏰ daily-notification.yml  # CI/CD automation pipeline
└── 🔐 environmentvariables.env    # Secure configuration store
```

### Component Overview

| Component | Purpose | Technology |
|-----------|---------|------------|
| **weather.py** | Real-time weather data fetching via WeatherAPI | REST API |
| **advice.py** | Intelligent clothing recommendations based on conditions | Python Logic |
| **tfl_status.py** | Live TfL service status monitoring | TfL Unified API |
| **notifier.py** | Cross-platform push notifications via Pushover | Pushover API |
| **daily_run.py** | GitHub Actions integration layer | Python + YAML |
| **iOS Shortcut** | Sends phone’s location to Supabase table | iOS Shorcuts App |

### Data Flow
```
Weather API → data_acquisition.py ──┐
                    ↑               │
📱 Phone Location → │               ├─→ advice.py → main.py → notifier.py → 📱 Your Device
(Lat/Long)          │               │                ↑
                    ↓               │                │
Google Maps API → Commute Time ─────┘                │
                                                     │
TfL API → tfl_status.py ─────────────────────────────┘
```


## Secrets & Environment Variables

The app uses the following environment variables (stored securely as GitHub Repository Secrets):

- `WEATHER_API_KEY` — Your WeatherAPI key
- `LAT` and `LON` — Coordinates for your location (e.g. London)
- `PUSHOVER_APP_TOKEN` — Token from your Pushover app
- `PUSHOVER_USER_KEY` — Your Pushover user key
- `TFL_APP_ID` and `TFL_APP_KEY` — Your credentials for the TfL API (optional)
- `GOOGLE_MAPS_API_KEY` - Your Google Maps API key
- `SUPABASE_API_KEY`, `SUPABASE_USER_ID` and `SUPABASE_URL`- Your credential for Supabase API 

---

## How It Works

1. GitHub Actions runs the workflow every morning at 7:00 AM (London time)
2. The workflow executes `daily_run.py`
3. This script:
   - Sends latitude and longitude coordinates to a Supabase table from your phone via iOS Shortcuts
   - Pulls the coordinates from the Supabase table and calculates commute time
   - Fetches today’s forecast and clothing advice
   - Retrieves the status of all London tube lines
   - Formats a summary message
   - Sends it to your phone via Pushover

---

## Example Notification

Good morning!

Today in London: 16°C, cloudy with a chance of rain.
Recommendation: Wear a light jacket and bring an umbrella.

Tube Status:

Victoria: Good Service

Central: Minor delays

Piccadilly: Part Closure ....

Your commute time is ... Route 1 ...

## Future Improvements

- Add alternative route suggestions if there are train cancellations or delays
- Add daily email report option

---

## Inspiration

This project was inspired by the idea of getting actionable insights (like what to wear or which tube line to avoid) before even getting out of bed.

---

## Author

**Neel Chudasama**  
This is a personal project for learning and automation purposes.  
Built with love using Python, GitHub Actions, and public APIs.
