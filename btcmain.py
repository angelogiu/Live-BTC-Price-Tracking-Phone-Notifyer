import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects, HTTPError
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
from telegram import Bot
from dotenv import load_dotenv
import time

load_dotenv()

#Can either enter API key, telegram bot token, and telegram chat ID directly
#into code or load on a .env

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"


parameters = {
  'id': 1,
  'convert':'CAD'
}

api_key = os.getenv("PRO_API_KEY")
if not api_key:
    raise RuntimeError("Missing PRO_API_KEY")

headers = {
    "Accept": "application/json",
    "X-CMC_PRO_API_KEY": api_key
}


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
if not TOKEN or not CHAT_ID:
    raise RuntimeError("missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID")

bot = Bot(token=TOKEN)

def send_telegram(msg):
    url2 = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.post(url2, data={"chat_id": CHAT_ID, "text": msg}, timeout=15)
    print("Telegram status:", r.status_code)
    if r.status_code != 200:
        print("Telegram error:", r.text)

    
session = Session()
session.headers.update(headers)

#API
def getBTCprice():
    try:
        response = session.get(url, params=parameters, timeout=15)
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["1"]["quote"]["CAD"]["price"])

    except (ConnectionError, Timeout, TooManyRedirects, HTTPError, KeyError, ValueError) as e:
        print("BTC fetch failed:", e)
        return None

times = []
prices = []
fig, ax = plt.subplots()
(line,) = ax.plot([], [], marker="o", linestyle="-")

ax.set_title("BTC Price Over Time")
ax.set_xlabel("Time")
ax.set_ylabel("Price (CAD)")

baselineprice = None
THRESHOLD = 0.01

def update(_frame):
    global baselineprice

    send_telegram("TEST ALERT — update reached alert block")

    price = getBTCprice()
    if price is None:
        return (line,)

    t = time.time()

    times.append(t)
    prices.append(price)
    line.set_data(times, prices)
    ax.relim()
    ax.autoscale_view()

    ax.set_xticks(times)
    ax.set_xticklabels(
        [time.strftime("%H:%M", time.localtime(ts)) for ts in times],
        rotation=45, ha="right"
    )

    print(f"{time.strftime('%H:%M:%S')}  BTC: {price:,.2f} CAD")
    
    if baselineprice is None:
        baselineprice = price
        return (line,)

    percent_change = (price - baselineprice) / baselineprice

    if abs(percent_change) >= THRESHOLD:
        direction = "up" if percent_change > 0 else "down"
        send_telegram(
                f"BTC moved {direction} {percent_change*100:.2f}% since last baseline.\n"
                f"Current: ${price:,.2f} CAD\n"
                f"Baseline: ${baselineprice:,.2f} CAD"
            
        )
        baselineprice = price
    return (line,)

ani = FuncAnimation(fig, update, interval=6000, blit=False)

plt.tight_layout()
plt.show()
