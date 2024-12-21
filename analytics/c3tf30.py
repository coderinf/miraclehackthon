import asyncio
import aiohttp
import pandas as pd

async def get_coins(session):
    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/active_instruments"
    async with session.get(url) as response:
        data = await response.json()
        return data

async def get_candle_data(session, pair):
    url = "https://public.coindcx.com/market_data/candlesticks"
    query_params = {
        "pair": pair,
        "from": (pd.Timestamp.now() - pd.Timedelta(hours=7, minutes=30)).timestamp(),
        "to": (pd.Timestamp.now() + pd.Timedelta(hours=0, minutes=15)).timestamp(),
        "resolution": "15",  # '1' OR '5' OR '60' OR '1D'
        "pcode": "f"
    }
    async with session.get(url, params=query_params) as response:
        if response.status == 200:
            data = await response.json()
            data = pd.DataFrame(data['data'])
            if data.empty is False:
                data['open'] = pd.to_numeric(data['open'])
                data['close'] = pd.to_numeric(data['close'])

                if data['close'][0] < data['close'][1] and data['low'][1] < data['low'] [2]< data['low'][3] and data['close'][1] < data['close'][2] < data[
                    'close'][3]:
                    return pair
                else:
                    return None
            else:
                return None
        else:
            return None

async def main():
    async with aiohttp.ClientSession() as session:
        coins = await get_coins(session)
        tasks = [get_candle_data(session, coin) for coin in coins]
        results = await asyncio.gather(*tasks)
        results = [result for result in results if result is not None]
        return results

def get_results():
    return asyncio.run(main())