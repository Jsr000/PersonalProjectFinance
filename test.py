import selenium
import yfinance as yf

msft = yf.Ticker("MSFT")
stock_beta = msft.info["beta"]