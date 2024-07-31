import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

API_KEY = 'a05f9e262c3019e6298c762e7b5911eb263ca30b3654f58f9b2ed4a8062d4c2c'
BASE_URL = 'https://min-api.cryptocompare.com/data/v2/histoday'

def fetch_historical_data(symbol, start_date, end_date):
    headers = {
        'Authorization': f'Apikey {API_KEY}'
    }
    params = {
        'fsym': symbol,
        'tsym': 'USD',
        'limit': 2000,  # Max number of data points per request
        'toTs': end_date,
        'since': start_date
    }
    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()
    return data

def save_data(data, filename):
    if 'Data' in data and 'Data' in data['Data']:
        df = pd.DataFrame(data['Data']['Data'])
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.to_csv(filename, index=False)
    else:
        print("Error: Unexpected data format")
        print(data)

end_date = datetime.now(timezone.utc).timestamp()
start_date = (datetime.now(timezone.utc) - timedelta(days=365)).timestamp()
data = fetch_historical_data('BTC', start_date, end_date)
save_data(data, 'btc_historical_data.csv')
