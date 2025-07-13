#main script this is the skeleton

from fastapi import FastAPI
from app.weather import get_weather_data
from app.notifier import send_notification
from app.advice import generate_clothing_advice

app = FastAPI()

@app.get("/send-morning-update")
def send_morning_update():
    weather = get_weather_data()
    advice = generate_clothing_advice(weather)
    send_notification(advice)
    return {"status": "Sent", "advice": advice}

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(send_morning_update, 'cron', hour=7, minute=0)
scheduler.start()

# Optional test endpoint
'''@app.get("/send-now")
def send_now():
    send_morning_update()
    return {"status": "sent manually"}

# Run locally
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)'''

