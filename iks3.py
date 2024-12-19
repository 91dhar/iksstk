import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Stock Price App

Shown are the stock closing prices and volume of ITC.

""")

tickerSymbol = 'IKS.BO'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2024-12-19', end='2024-12-19')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
# 
Shown are the stock closing prices and volume of TATA Motors, India.

""")

tickerSymbol = 'ITC.BO'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2024-12-19', end='2024-12-19')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)