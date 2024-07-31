import requests
import pandas as pd
from datetime import datetime, timedelta

# Pull API key
API_KEY = '4a0a4cd7-2c3e-4138-bdef-bc11a154ece3'
BASE_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical'

def fetch_historical_data(symbol, start_date, end_date, interval='daily'):
    headers = {
        'X-CMC_PRO_API_KEY': API_KEY
    }
    params = {
        'symbol': symbol,
        'time_start': start_date,
        'time_end': end_date,
        'interval': interval
    }
    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()
    return data

def save_data(data, filename):
    df = pd.DataFrame(data['data']['quotes'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.to_csv(filename, index=False)

# Fetch data for the last year
end_date = datetime.utcnow()
start_date = end_date - timedelta(days=365)
data = fetch_historical_data('BTC', start_date.isoformat(), end_date.isoformat())
save_data(data, 'btc_historical_data.csv')
