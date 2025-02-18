import yfinance as yf
import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import date, timedelta

selectedTickerInput = input("Enter ticker: ")
ticker = yf.Ticker(selectedTickerInput)
ticker.history(period="1d", interval="1m")

data = yf.download(selectedTickerInput, '2024-04-03', '2024-05-03').info

df = pd.DataFrame([data])
df.to_csv(selectedTickerInput + "Data.csv", index=False, encoding='utf-8')


tickerPrice = ticker.info.get("currentPrice")
print(tickerPrice)
