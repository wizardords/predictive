import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['close'])
plt.title('Bitcoin Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.show()
