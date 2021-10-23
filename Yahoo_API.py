import json
import yfinance as yf

print('y finance version' + yf.__version__)

stock=yf.Ticker(input('Stock name='))
stock_info=stock.info
close_price=stock_info['previousClose']
print(stock_info)
print(close_price)