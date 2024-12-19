import yfinance as yf
import time
import schedule
from flask import Flask, render_template
import yfinance as yf

def get_stock_price(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    # Fetch the latest market data
    data = stock.history(period='1d', interval='1m')  # '1m' for 1-minute intervals
    latest_data = data.tail(1)  # Get the latest record
    price = latest_data['Close'].iloc[0]  # Use the closing price
    return price

ticker = "IKS.BO"  # Replace with your stock ticker
price = get_stock_price(ticker)
print(f"The latest price of {ticker} is INR{price:.2f}")

def track_stock_price():
    ticker = "IKS.BO"
    price = get_stock_price(ticker)
    print(f"The latest price of {ticker} is INR{price:.2f}")

schedule.every(1).minute.do(track_stock_price)

print("Starting stock price tracker...")
while True:
    schedule.run_pending()
    time.sleep(1)

app = Flask(__name__)

def get_stock_price(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    data = stock.history(period='1d', interval='1m')
    latest_data = data.tail(1)
    price = latest_data['Close'].iloc[0]
    return price

@app.route('/')
def home():
    ticker = "IKS.BO"  # Replace with your desired ticker
    price = get_stock_price(ticker)
    return render_template('index.html', ticker=ticker, price=price)

if __name__ == '__main__':
    app.run(debug=True)