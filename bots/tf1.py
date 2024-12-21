import asyncio
import aiohttp
import pandas as pd
import requests
from datetime import datetime
import emoji
from flask import Flask, render_template
app = Flask(__name__)

green_heart = emoji.emojize(":green_heart:")
red_heart = emoji.emojize(":red_heart:")

purl = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/active_instruments"
response = requests.get(purl)
data = response.json()
pairs = list(data)

msgs = ""

def send_signal_message(symbol, signal_value, side, heart):
    global msgs
    message = f"{symbol} {signal_value:.2f}% {side}{heart}"
    msgs += message + "\n"

async def fetch_candlestick(pair, session):
    url = "https://public.coindcx.com/market_data/candlesticks"
    query_params = {
        "pair": str(pair),
        "from": (pd.Timestamp.now() - pd.Timedelta(hours=7)).timestamp(),
        "to": (pd.Timestamp.now() + pd.Timedelta(hours=0, minutes=7)).timestamp(),
        "resolution": "60",  # '1' OR '5' OR '60' OR '1D'
        "pcode": "f"
    }
    async with session.get(url, params=query_params) as response:
        if response.status == 200:
            data = await response.json()
            data = pd.DataFrame(data['data'])
            if not data.empty:
                data['open'] = pd.to_numeric(data['open'])
                data['close'] = pd.to_numeric(data['close'])
                data['signal'] = ((data['close'] - data['open']) / data['open']) * 100
                if data['signal'][0] > 1.0:
                    send_signal_message(pair, data['signal'][0], "LONG", green_heart)
                elif data['signal'][0] < -1.0:
                    send_signal_message(pair, data['signal'][0], "SHORT", red_heart)
        else:
            print(f"Error fetching data for {pair}: {response.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_candlestick(pair, session) for pair in pairs]
        await asyncio.gather(*tasks)
    return msgs
def get_signals():
    return asyncio.run(main())