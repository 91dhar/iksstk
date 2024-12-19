import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import yfinance as yf
import threading
import pandas as pd
import time


# Function to fetch stock data for the day
def fetch_stock_data(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)
        data = stock.history(period="1d", interval="1m")  # 1-day, 1-minute interval
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")
        return None


# Function to update the chart
def update_chart():
    ticker = "IKS.BO"  # Static ticker for IKS.BO

    def fetch_and_plot():
        while True:
            data = fetch_stock_data(ticker)
            if data is not None:
                prices = data["Close"]
                times = pd.to_datetime(data.index)

                # Clear and redraw the chart
                ax.clear()
                ax.plot(times, prices, label="Price")
                ax.set_title(f"{ticker} Price Chart (INR)", fontsize=14)
                ax.set_xlabel("Time", fontsize=12)
                ax.set_ylabel("Price (₹)", fontsize=12)
                ax.grid(True)
                ax.legend()

                canvas.draw()
            time.sleep(60)  # Refresh every 60 seconds

    threading.Thread(target=fetch_and_plot, daemon=True).start()


# Function to stop the application
def quit_app():
    root.quit()


# Tkinter setup
root = tk.Tk()
root.title("Stock Price Tracker - IKS.BO")
root.geometry("800x600")

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(8, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# UI Buttons
tk.Button(root, text="Start Tracking", font=("Arial", 12), command=update_chart).pack(pady=10)
tk.Button(root, text="Quit", font=("Arial", 12), command=quit_app).pack(pady=10)

# Run the application
root.mainloop()
