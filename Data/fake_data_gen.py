import pandas as pd
import numpy as np
from datetime import time

# Define the date range (last 5 years from today)
end_date = pd.Timestamp.today().normalize()
start_date = end_date - pd.DateOffset(years=5)

# Generate a range of business days between start and end dates
business_days = pd.date_range(start=start_date, end=end_date, freq='B')

# Define trading hours (example: 9:30 AM to 4:00 PM)
trading_start = time(9, 30)
trading_end = time(16, 0)

# Create a list to collect all minute timestamps during trading hours for each business day
timestamps = []
for day in business_days:
    day_start = pd.Timestamp.combine(day, trading_start)
    day_end = pd.Timestamp.combine(day, trading_end)
    day_minutes = pd.date_range(start=day_start, end=day_end, freq='T')
    timestamps.extend(day_minutes)

# Create a DataFrame index from the collected timestamps
index = pd.DatetimeIndex(timestamps)

# Set random seed for reproducibility
np.random.seed(42)

# Number of data points
n = len(index)

# Simulate an open price as a random walk starting at 100
open_prices = np.empty(n)
open_prices[0] = 100  # initial price

# Simulate changes with a small Gaussian noise (drift=0, small volatility)
for i in range(1, n):
    open_prices[i] = open_prices[i - 1] + np.random.normal(0, 0.1)

# Simulate high and low prices based on the open
# High is open plus a positive noise; low is open minus a positive noise.
high_prices = open_prices + np.abs(np.random.normal(0, 0.2, n))
low_prices = open_prices - np.abs(np.random.normal(0, 0.2, n))

# Simulate close prices as a random value between low and high
close_prices = np.random.uniform(low_prices, high_prices)

# Create a DataFrame to hold the simulated data
df = pd.DataFrame({
    'Open': open_prices,
    'High': high_prices,
    'Low': low_prices,
    'Close': close_prices
}, index=index)

# Save the DataFrame to a CSV file
df.to_csv('coffee_futures_minute_data.csv')
print("Data saved to coffee_futures_minute_data.csv")
