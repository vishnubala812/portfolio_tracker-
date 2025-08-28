import streamlit as st
import yfinance as yf
import pandas as pd
import os, json

DATA_FILE = "data/portfolio.json"

# Ensure data file exists
os.makedirs("data", exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_portfolio():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_portfolio(portfolio):
    with open(DATA_FILE, "w") as f:
        json.dump(portfolio, f, indent=4)

st.title("📈 Indian Stock Portfolio Tracker (NSE + BSE)")

portfolio = load_portfolio()

with st.form("add_stock"):
    ticker = st.text_input("Enter Stock Symbol (e.g., RELIANCE, TCS, 500325.BO)").upper()
    qty = st.number_input("Quantity", min_value=1, step=1)
    conviction = st.slider("Conviction Level", 1, 5, 3)
    notes = st.text_area("Investment Thesis / Notes")
    submitted = st.form_submit_button("Add to Portfolio")

    if submitted and ticker:
        portfolio.append({
            "ticker": ticker,
            "qty": qty,
            "conviction": conviction,
            "notes": notes
        })
        save_portfolio(portfolio)
        st.success(f"Added {ticker} to portfolio!")

if portfolio:
    df = pd.DataFrame(portfolio)
    prices = []
    for t in df["ticker"]:
        try:
            data = yf.Ticker(t).history(period="1d")
            prices.append(round(data["Close"].iloc[-1], 2))
        except:
            prices.append(None)
    df["Live Price"] = prices
    st.dataframe(df)
else:
    st.info("No stocks in portfolio yet. Add one above!")
