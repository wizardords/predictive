import pandas as pd

# Load the data
df = pd.read_csv('btc_historical_data.csv')

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Keeping only the relevant columns
df = df[['timestamp', 'quote.USD.close']]
df.columns = ['timestamp', 'close']

# Check for null values in data
df = df.dropna()

print(df.head())
