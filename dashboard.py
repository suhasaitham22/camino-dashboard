import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def authenticate_google_sheets():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'credentials.json', scope)
    client = gspread.authorize(creds)
    return client.open('dashboard export').sheet1  # Replace with your own sheet name

sheet = authenticate_google_sheets()
data = sheet.get_all_records()
df = pd.DataFrame(data)

st.write(df)