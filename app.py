import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="ThesisOS", layout="wide")

st.title("📊 ThesisOS — Investment Thesis Builder")

ticker = st.text_input("Enter Stock Ticker (e.g. AAPL)")

if ticker:
    stock = yf.Ticker(ticker)
    info = stock.info

    col1, col2, col3 = st.columns(3)

    col1.metric("Company", info.get("shortName", "N/A"))
    col2.metric("Sector", info.get("sector", "N/A"))
    col3.metric("Country", info.get("country", "N/A"))

    st.divider()

    tabs = st.tabs([
        "🌍 Macro",
        "🛢️ Commodities",
        "🏭 Supply Chain",
        "📊 Financials",
        "⚠️ Risks",
        "✅ Decision"
    ])

    with tabs[0]:
        st.write("Macro Regime (rule-based)")
        st.selectbox("Inflation Trend", ["Rising", "Falling", "Sticky"])
        st.selectbox("Rates Outlook", ["Tightening", "Neutral", "Easing"])

    with tabs[1]:
        st.write("Commodity Exposure")
        st.multiselect("Key Inputs", ["Oil", "Gas", "Copper", "Agriculture"])

    with tabs[2]:
        st.slider("Supply Chain Pressure", 1, 5, 3)
        st.text_area("Key Bottlenecks")

    with tabs[3]:
        st.metric("Gross Margin", f"{info.get('grossMargins', 0)*100:.1f}%")
        st.metric("Debt / Equity", info.get("debtToEquity", "N/A"))

    with tabs[4]:
        st.text_area("Key Risks")

    with tabs[5]:
        st.selectbox("Decision", ["Accumulate", "Watch", "Avoid"])
        st.slider("Confidence", 1, 5, 3)
        st.text_area("Final Thesis Summary")
