import streamlit as st
import yfinance as yf
import pandas as pd
import json
import os

DATA_FILE = "portfolio.json"

def load_portfolio():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_portfolio(portfolio):
    with open(DATA_FILE, "w") as f:
        json.dump(portfolio, f, indent=4)

st.title("📈 Indian Stock Portfolio Tracker (NSE/BSE)")

portfolio = load_portfolio()

with st.form("add_stock"):
    ticker = st.text_input("Stock Ticker (e.g. RELIANCE, TCS, SBIN.BO)")
    qty = st.number_input("Quantity", min_value=1, step=1)
    buy_price = st.number_input("Buy Price", min_value=0.0, format="%.2f")
    notes = st.text_area("Investment Thesis / Notes")
    conviction = st.slider("Conviction (1-5)", 1, 5, 3)
    submitted = st.form_submit_button("Add Stock")
    if submitted:
        portfolio.append({
            "ticker": ticker,
            "qty": qty,
            "buy_price": buy_price,
            "notes": notes,
            "conviction": conviction
        })
        save_portfolio(portfolio)
        st.success(f"Added {ticker}")

if portfolio:
    st.subheader("Current Portfolio")
    df = pd.DataFrame(portfolio)
    tickers = [p["ticker"] + (".NS" if not p["ticker"].endswith(".BO") and not p["ticker"].endswith(".NS") else "") for p in portfolio]
    prices = {}
    for t in tickers:
        try:
            prices[t] = yf.Ticker(t).history(period="1d")["Close"].iloc[-1]
        except:
            prices[t] = None
    values = []
    for p, t in zip(portfolio, tickers):
        price = prices.get(t)
        current_val = p["qty"] * price if price else None
        values.append(current_val)
    df["Current Price"] = [prices[t] for t in tickers]
    df["Current Value"] = values
    st.dataframe(df)
