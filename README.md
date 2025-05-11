from flask import Flask, render_template, request, jsonify, send_from_directory
import threading
import time
import pandas as pd
import requests
import datetime
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# CONFIG
TOTAL_UNITS = 100
UNITS_LEFT = TOTAL_UNITS
REVENUE = 0.0
TRADE_INTERVAL = 2  # seconds
TRADE_DURATION = 10 * 60  # 10 minutes
SELL_ENDPOINT = "https://api.example.com/sell"
PRICE_ENDPOINT = "https://api.example.com/live_price"

# For simulation
historical_df = pd.DataFrame(columns=['datetime', 'current_value'])  # placeholder for real CSV load
try:
    historical_df = pd.read_csv("historical_data.csv")
    historical_df['datetime'] = pd.to_datetime(historical_df['datetime'])
except FileNotFoundError:
    pass

# Globals for live tracking
live_data = []
sell_log = []
start_time = None

def decide_units_to_sell(current_price, avg_price, units_left):
    if current_price > avg_price * 1.01:
        return min(10, units_left)
    elif current_price > avg_price:
        return min(5, units_left)
    elif current_price > avg_price * 0.99:
        return min(2, units_left)
    return 0

def simulate_trading():
    global UNITS_LEFT, REVENUE, sell_log
    UNITS_LEFT = TOTAL_UNITS
    REVENUE = 0.0
    sell_log = []

    avg_price = historical_df['current_value'].mean()
    for i in range(min(len(historical_df), TRADE_DURATION // TRADE_INTERVAL)):
        row = historical_df.iloc[i]
        price = row['current_value']
        units_to_sell = decide_units_to_sell(price, avg_price, UNITS_LEFT)
        UNITS_LEFT -= units_to_sell
        REVENUE += units_to_sell * price
        sell_log.append({"time": row['datetime'].strftime('%H:%M:%S'), "price": price, "units": units_to_sell, "revenue": REVENUE})
        if UNITS_LEFT <= 0:
            break
        time.sleep(TRADE_INTERVAL)

def live_trading():
    global UNITS_LEFT, REVENUE, start_time, sell_log
    UNITS_LEFT = TOTAL_UNITS
    REVENUE = 0.0
    sell_log = []
    start_time = datetime.datetime.now()
    avg_price = 0.0
    prices = []

    while (datetime.datetime.now() - start_time).total_seconds() < TRADE_DURATION and UNITS_LEFT > 0:
        try:
            res = requests.get(PRICE_ENDPOINT)
            data = res.json()
            price = data["current_value"]
            prices.append(price)
            avg_price = sum(prices) / len(prices)

            units_to_sell = decide_units_to_sell(price, avg_price, UNITS_LEFT)
            if units_to_sell > 0:
                sell_payload = {"units": units_to_sell}
                requests.post(SELL_ENDPOINT, json=sell_payload)
                UNITS_LEFT -= units_to_sell
                REVENUE += units_to_sell * price
                sell_log.append({"time": datetime.datetime.now().strftime('%H:%M:%S'), "price": price, "units": units_to_sell, "revenue": REVENUE})
        except Exception as e:
            print("Error during trading:", e)
        time.sleep(TRADE_INTERVAL)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_simulation")
def start_simulation():
    threading.Thread(target=simulate_trading).start()
    return jsonify({"status": "Simulation started"})

@app.route("/start_live")
def start_live():
    threading.Thread(target=live_trading).start()
    return jsonify({"status": "Live trading started"})

@app.route("/status")
def status():
    return jsonify({"units_left": UNITS_LEFT, "revenue": REVENUE, "sell_log": sell_log})

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    os.makedirs("templates", exist_ok=True)
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
