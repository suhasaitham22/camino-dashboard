import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import time
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# def authenticate_google_sheets():
#     scope = ['https://spreadsheets.google.com/feeds',
#              'https://www.googleapis.com/auth/drive']
#     creds = ServiceAccountCredentials.from_json_keyfile_name(
#         'credentials.json', scope)
#     client = gspread.authorize(creds)
#     return client.open('dashboard export').sheet1  # Replace with your own sheet name

df=pd.read_excel('C:\Users\SUHAS\Downloads\camino dashboard\dashboard export.xlsx')

st.set_page_config(
    page_title = 'CAMINO LCSNA Real-Time Dashboard',
    page_icon= '*',
    layout='wide'
)

st.title('Real-Time LCSNA Dahboard')

county_filter = st.selectbox('Select a County', pd.unique(df['County']))

placeholder=st.empty()

df = df[df['County']==county_filter]

st.write(df)
