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
    page_title='CAMINO LCSNA Real-Time Dashboard',
    page_icon='*',
    layout='wide'
)

# Sidebar navigation
page = st.sidebar.selectbox('Page', ('Home', 'Gender Differences', 'Residency Differences'))

# Home Page
if page == 'Home':
    st.title('Home')
    st.header('About Camino Research Institute')
    st.write('Add a brief description of the Camino Research Institute here.')
    
    st.header('Data Collection Methodology')
    st.write('Describe the data collection methodology used by the Camino Research Institute here.')
    
    st.header('Team Members')
    st.write('Introduce the team members of the Camino Research Institute here.')

# Gender Differences Page
elif page == 'Gender Differences':
    st.title('Gender Differences')
    # Add content specific to the Gender Differences page here
    
# Residency Differences Page
elif page == 'Residency Differences':
    st.title('Residency Differences')
    # Add content specific to the Residency Differences page here
