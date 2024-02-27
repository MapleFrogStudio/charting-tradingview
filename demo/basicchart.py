# https://hackingthemarkets.com/interactive-brokers-api-tradingview-charts-in-python/

import pandas as pd
import pandas_ta as ta
import yfinance as yf
from lightweight_charts import Chart

url = 'https://raw.githubusercontent.com/louisnw01/lightweight-charts-python/main/examples/1_setting_data/ohlcv.csv'

if __name__ == '__main__':
    
    chart = Chart()
    
    # Columns: time | open | high | low | close | volume 
    df = pd.read_csv(url)
    chart.set(df)
    
    chart.show(block=True)
