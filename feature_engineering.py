import numpy as np

# Create lag features
for lag in range(1, 8):
    df[f'lag_{lag}'] = df['close'].shift(lag)

# Drop rows with missing values
df = df.dropna()

# Split into features and target
X = df.drop(['timestamp', 'close'], axis=1)
y = df['close']

print(X.head())
print(y.head())
