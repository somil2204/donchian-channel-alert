import yfinance as yf

def get_csv1(ticker,period,interval):
    ticker = yf.Ticker(str(ticker)+".NS")
    hist = ticker.history(period=period,interval=interval)
    return hist

   