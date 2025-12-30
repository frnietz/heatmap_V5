import streamlit as st
import yfinance as yf
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="ThesisOS",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

/* --- Global --- */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #0E1117;
    color: #E6E6E6;
}

/* Remove Streamlit default UI */
#MainMenu, footer, header {
    visibility: hidden;
}

/* Headings */
h1, h2, h3 {
    font-weight: 600;
    letter-spacing: -0.02em;
}

/* --- Cards --- */
.card {
    background: #161B22;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 0 0 1px rgba(255,255,255,0.04);
}

/* --- Metric Cards --- */
.metric {
    background: #161B22;
    border-radius: 12px;
    padding: 16px;
    text-align: center;
}

.metric-title {
    font-size: 13px;
    color: #8B949E;
}

.metric-value {
    font-size: 20px;
    font-weight: 600;
    margin-top: 4px;
}

/* --- Inputs --- */
input, textarea, select {
    background-color: #0E1117 !important;
    border-radius: 10px !important;
    border: 1px solid #30363D !important;
    color: #E6E6E6 !important;
}

/* --- Buttons --- */
.stButton>button {
    background: linear-gradient(135deg, #3B82F6, #2563EB);
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 18px;
    font-weight: 600;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #2563EB, #1D4ED8);
}

/* --- Tabs --- */
.stTabs [data-baseweb="tab"] {
    font-size: 14px;
    padding: 12px;
    color: #8B949E;
}

.stTabs [aria-selected="true"] {
    color: #E6E6E6;
    border-bottom: 2px solid #3B82F6;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<div class="card">
    <h2>📊 ThesisOS</h2>
    <p style="color:#8B949E;">
        Automated Investment Thesis Builder<br>
        Macro → Commodities → Supply Chain → Company → Decision
    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# INPUT CARD
# --------------------------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 1])

ticker = col1.text_input("Stock Ticker", placeholder="AAPL, MSFT, NVDA")
horizon = col2.selectbox("Time Horizon", ["Short", "Medium", "Long"])
generate = col3.button("Generate Thesis")

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# MAIN LOGIC
# --------------------------------------------------
if generate and ticker:

    try:
        stock = yf.Ticker(ticker)
        info = stock.info
    except Exception as e:
        st.error("Failed to fetch data. Please check the ticker.")
        st.stop()

    company = info.get("shortName", "N/A")
    sector = info.get("sector", "N/A")
    country = info.get("country", "N/A")
    currency = info.get("currency", "N/A")
    gross_margin = info.get("grossMargins", 0)
    debt_equity = info.get("debtToEquity", "N/A")

    # --------------------------------------------------
    # SUMMARY METRICS
    # --------------------------------------------------
    col1, col2, col3, col4 = st.columns(4)

    col1.markdown(f"""
    <div class="metric">
        <div class="metric-title">Company</div>
        <div class="metric-value">{company}</div>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown(f"""
    <div class="metric">
        <div class="metric-title">Sector</div>
        <div class="metric-value">{sector}</div>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
    <div class="metric">
        <div class="metric-title">Country</div>
        <div class="metric-value">{country}</div>
    </div>
    """, unsafe_allow_html=True)

    col4.markdown(f"""
    <div class="metric">
        <div class="metric-title">Currency</div>
        <div class="metric-value">{currency}</div>
    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------------
    # TABS
    # --------------------------------------------------
    tabs = st.tabs([
        "🌍 Macro",
        "🛢️ Commodities",
        "🏭 Supply Chain",
        "📊 Financials",
        "⚠️ Risks",
        "✅ Decision"
    ])

    # -------------------- MACRO --------------------
    with tabs[0]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        inflation = st.selectbox("Inflation Trend", ["Rising", "Falling", "Sticky"])
        rates = st.selectbox("Interest Rates Outlook", ["Tightening", "Neutral", "Easing"])
        macro_note = st.text_area(
            "Key Macro Insight",
            placeholder="What macro force matters most for this asset?"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------- COMMODITIES --------------------
    with tabs[1]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        commodities = st.multiselect(
            "Key Commodity Exposures",
            ["Oil", "Natural Gas", "Copper", "Aluminum", "Agriculture", "Metals"]
        )
        commodity_note = st.text_area(
            "Commodity Insight",
            placeholder="Which input cost or commodity trend can surprise the market?"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------- SUPPLY CHAIN --------------------
    with tabs[2]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        supply_stress = st.slider("Supply Chain Stress Level", 1, 5, 3)
        bottlenecks = st.text_area(
            "Bottlenecks / Constraints",
            placeholder="Capacity, logistics, suppliers, inventory issues..."
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------- FINANCIALS --------------------
    with tabs[3]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.metric("Gross Margin", f"{gross_margin*100:.1f}%")
        st.metric("Debt / Equity", debt_equity)
        fin_note = st.text_area(
            "Financial Insight",
            placeholder="What does the market misunderstand about the financials?"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------- RISKS --------------------
    with tabs[4]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        risks = st.text_area(
            "Key Risks & Scenarios",
            placeholder="Bear case, invalidation triggers, tail risks..."
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------- DECISION --------------------
    with tabs[5]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        decision = st.selectbox("Final Decision", ["Accumulate", "Watch", "Avoid"])
        confidence = st.slider("Confidence Level", 1, 5, 3)
        thesis = st.text_area(
            "Final Investment Thesis",
            placeholder="Clear, structured, unemotional reasoning..."
        )
        st.button("Save Thesis (v1)")
        st.markdown("</div>", unsafe_allow_html=True)
