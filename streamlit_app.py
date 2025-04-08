import pandas as pd
import streamlit as st
import os

# Read the CSV files assuming they are in the same directory as streamlit_app.py
price_data = pd.read_csv("20250408_CBA_HISTORICAL DATA.csv")
star_data = pd.read_csv("20250408_Phillip Dwyer_STAR CHARTS.csv")

# Display in app
st.title("Hermetic Trading System")
st.subheader("CBA Historical Price Data")
st.dataframe(price_data)

st.subheader("Phillip Dwyer Star Charts")
st.dataframe(star_data)
