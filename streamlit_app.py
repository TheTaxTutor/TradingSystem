import streamlit as st
import pandas as pd
import os

st.title("Hermetic Trading System")

# Load your data
data_folder = "data"
cba_data = pd.read_csv(os.path.join(data_folder, "20250408_CBA_HISTORICAL DATA.csv"))
stars_data = pd.read_csv(os.path.join(data_folder, "20250408_Phillip Dwyer_STAR CHARTS.csv"))

# Preview data
st.subheader("CBA Data")
st.write(cba_data.head())

st.subheader("Star Chart Data")
st.write(stars_data.head())
