import pandas as pd
import matplotlib.pyplot as plt

# Load the preprocessed data
df = pd.read_csv('btc_preprocessed_data.csv')

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['close'])
plt.title('Bitcoin Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.show()
