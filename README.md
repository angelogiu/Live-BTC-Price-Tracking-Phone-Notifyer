# Crypto Price Tracker & Telegram Alert Bot 🚀

A lightweight Python project that tracks live cryptocurrency prices, plots them in real time, and sends Telegram alerts when prices move beyond a set threshold.

Built as a practical exercise in working with APIs, automation, and real-time data visualization.

<table>
  <tr>
    <td align="center">
      <img src="images/screenshot.png" width="400"/><br/>
      <sub>Live price tracking</sub>
    </td>
    <td align="center">
      <img src="images/IMG_2067.PNG" width="400"/><br/>
      <sub>Telegram alert notification</sub>
    </td>
  </tr>
</table>

---

## What This Project Does

* Pulls live crypto prices from the CoinMarketCap API
* Displays price movement on a real-time chart
* Sends Telegram alerts when prices move up or down by a chosen percentage
* Lets the user control:

  * Which coin to track
  * How often prices are checked
  * When alerts should trigger

---

## Supported Coins

* Bitcoin (BTC)
* Ethereum (ETH)
* Binance Coin (BNB)
* Tether (USDT)

---

## How It Works

1. User selects a coin, alert threshold, and time interval
2. The app polls live prices at the chosen interval
3. Prices are plotted over time
4. When the price moves enough:

   * A Telegram message is sent
   * The baseline price resets
---

## Setup

### Install Dependencies

```bash
pip install requests numpy matplotlib python-dotenv python-telegram-bot
```

### Create a `.env` File

```env
PRO_API_KEY=your_coinmarketcap_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

## Run the App

```bash
python main.py
```

You’ll be prompted to choose:

* A cryptocurrency
* A percentage threshold for alerts
* A polling interval (seconds)

A live chart will open, and alerts will arrive on Telegram automatically.

---

## Example Alert

```
BTC moved up 0.52%
Current: $95,234.12 CAD
Baseline: $94,738.91 CAD
```
