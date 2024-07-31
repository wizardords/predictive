import pandas as pd

# Load the CSV file
df = pd.read_csv('btc_historical_data.csv')

# Convert 'time' to datetime
df['time'] = pd.to_datetime(df['time'])

# Select relevant columns
df = df[['time', 'close']]
df.columns = ['timestamp', 'close']

# Drop any rows with missing values
df = df.dropna()

# Save the preprocessed data
df.to_csv('btc_preprocessed_data.csv', index=False)
