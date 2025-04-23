import streamlit as st
import yfinance as yf
import plotly.express as px


tab1, tab2 = st.tabs(["Tab 1: Yahoo: información de stocks", "Tab 2: Mercados"])
with tab1:
    # Section 1: Header
    st.title("Yahoo info market")

    # Section 2: About
    st.header("Stocks price")    
    url = "https://finance.yahoo.com/markets/"
    st.write("Info de stocks [link](%s)" % url)
    # Divider
    st.markdown("---")
    st.markdown("Info de stocks [link](%s)" % url)


with tab2:
    st.title("Stock Price Tracker")
    ticker = st.text_input("Ingresa el symbol (e.g., NVDA, BTC-USD)", "NVDA")

    if ticker:
        stock = yf.Ticker(ticker)
        df_stocks = stock.history(period="1y")
        st.write("graficando con streamlit.line_chart")
        st.line_chart(df_stocks['Close'])
        st.write("graficando con Plotly")
        fig = px.line(df_stocks)

        st.plotly_chart(fig)

        st.write("Stock Data Summary:", df_stocks.head(5))
        st.write("Stock Data Summary:", df_stocks.describe())
        st.write("Stock Data Summary:", df_stocks.columns)