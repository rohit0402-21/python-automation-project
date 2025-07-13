import yfinance as yf
import pandas as pd

# Download GOLD (XAU/USD futures) 15-minute data for last 60 days
df = yf.download("GC=F", interval="15m", period="60d")

# Display first few rows
print(df.head())

# Save it for backtesting
df.to_csv("gold_15min.csv")

print("15-min Gold data downloaded and saved as gold_15min.csv")
