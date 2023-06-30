import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import time

def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

st.set_page_config(
    page_title = 'CAMINO LCSNA Real-Time Dashboard',
    page_icon= '*',
    layout='wide'
)

st.title('Real-Time LCSNA Dahboard')

st.write(df)
