import pandas as pd

# Load the preprocessed data
df = pd.read_csv('btc_preprocessed_data.csv')

# Create lag features
for lag in range(1, 8):
    df[f'lag_{lag}'] = df['close'].shift(lag)

# Drop rows with NaN values
df = df.dropna()

# Split features and target variable
X = df.drop(['timestamp', 'close'], axis=1)
y = df['close']

# Save features and target variable
X.to_csv('btc_features.csv', index=False)
y.to_csv('btc_target.csv', index=False)
