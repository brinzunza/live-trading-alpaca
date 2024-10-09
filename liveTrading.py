import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta
import time
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame

# Alpaca API credentials
ALPACA_API_KEY = 'api-key'
ALPACA_SECRET_KEY = 'secret-key'
ALPACA_BASE_URL = 'https://paper-api.alpaca.markets'

# Initialize Alpaca API
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, api_version='v2')

def buy(symbol, qty):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    return(f"Bought {qty} shares of {symbol}")

def sell(symbol, qty):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='market',
        time_in_force='gtc'
    )
    return(f"Sold {qty} shares of {symbol}")

if __name__ == "__main__":
    buy('BTC/USD', 1)
