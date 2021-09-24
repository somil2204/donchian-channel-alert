import yfinance as yf

def get_csv1(ticker):
    ticker = yf.Ticker(str(ticker)+".NS")
    hist = ticker.history(period="3mo")
    return hist

   