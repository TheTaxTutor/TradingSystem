import pandas as pd
import streamlit as st
import os

st.set_page_config(page_title="Hermetic Trading System", layout="wide")
st.title("Hermetic Trading System")

try:
    st.write("Current working directory:", os.getcwd())

    # Check if files exist
    if os.path.exists("20250408_CBA_HISTORICAL DATA.csv"):
        st.success("Found CBA Historical Data")
        price_data = pd.read_csv("20250408_CBA_HISTORICAL DATA.csv")
        st.dataframe(price_data)
    else:
        st.error("❌ Missing: 20250408_CBA_HISTORICAL DATA.csv")

    if os.path.exists("20250408_Phillip Dwyer_STAR CHARTS.csv"):
        st.success("Found Star Charts Data")
        star_data = pd.read_csv("20250408_Phillip Dwyer_STAR CHARTS.csv")
        st.dataframe(star_data)
    else:
        st.error("❌ Missing: 20250408_Phillip Dwyer_STAR CHARTS.csv")

except Exception as e:
    st.exception(e)
