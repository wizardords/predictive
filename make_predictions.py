import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load the data and model
df = pd.read_csv('btc_preprocessed_data.csv')
last_row = df.iloc[-1].drop(['timestamp', 'close'])

X = pd.read_csv('btc_features.csv')
y = pd.read_csv('btc_target.csv', squeeze=True)

# Re-train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Predict the next day's price
next_day_prediction = model.predict(last_row.values.reshape(1, -1))
print(f'Next Day Prediction: {next_day_prediction[0]}')
