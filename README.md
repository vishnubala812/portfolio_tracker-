# 📈 Indian Stock Portfolio Tracker (NSE + BSE)

This is a simple Streamlit app to track your stock portfolio with investment thesis & conviction levels.  
Supports NSE (use `RELIANCE`, `TCS`, etc.) and BSE (append `.BO`, e.g., `500325.BO`).

## Features
- Add / edit / delete stock positions
- Track conviction (1–5) & thesis notes
- Fetch live NSE/BSE prices from Yahoo Finance
- Summarize portfolio performance

## Deploy on Streamlit Cloud
1. Upload this repo to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Create new app → point to `app.py`.
4. Done ✅

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
