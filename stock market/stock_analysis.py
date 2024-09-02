import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbol and time period
stock_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2024-01-01'

# Fetch stock data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Display the first few rows of the dataframe
print(stock_data.head())


# Calculate 20-day and 50-day moving averages
stock_data['SMA20'] = stock_data['Close'].rolling(window=20).mean()
stock_data['SMA50'] = stock_data['Close'].rolling(window=50).mean()


# Plot closing price and moving averages
plt.figure(figsize=(14, 7))

# Plot the closing price
plt.plot(stock_data['Close'], label='Close Price', color='blue', linewidth=2)

# Plot 20-day moving average
plt.plot(stock_data['SMA20'], label='20-Day SMA', color='red', linestyle='--')

# Plot 50-day moving average
plt.plot(stock_data['SMA50'], label='50-Day SMA', color='green', linestyle='--')

# Add title and labels
plt.title('Apple Inc. (AAPL) Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
