import tkinter as tk
import yfinance as yf


class StockTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Tracker")

        self.stock_label = tk.Label(root, text="Enter Stock Symbol:")
        self.stock_label.pack()

        self.stock_entry = tk.Entry(root)
        self.stock_entry.pack()

        self.track_button = tk.Button(
            root, text="Track Stock", command=self.track_stock)
        self.track_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def track_stock(self):
        stock_symbol = self.stock_entry.get()
        stock_data = yf.Ticker(stock_symbol)
        stock_price = stock_data.history(period="1d")['Close'][0]
        self.result_label.config(
            text=f"Current price of {stock_symbol}: INR{stock_price:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = StockTrackerApp(root)
    root.mainloop()
