import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import requests
import io

def load_data(sheets_url):
    try:
        excel_url = sheets_url.replace("/edit#gid=", "/export?format=xlsx&gid=")
        response = requests.get(excel_url)
        content = response.content
        df = pd.read_excel(io.BytesIO(content), engine='xlrd')
        return df
    except (requests.exceptions.RequestException, pd.errors.ParserError) as e:
        st.error("Error: Failed to load data from the Excel file.")
        st.error(str(e))
        return None

# Check if the 'public_gsheets_url' secret is available
if "public_gsheets_url" not in st.secrets:
    st.error("Error: 'public_gsheets_url' secret not found.")
else:
    # Get the URL from the secret
    sheets_url = st.secrets["public_gsheets_url"]
    
    df = load_data(sheets_url)

    if df is not None:
        st.set_page_config(
            page_title='CAMINO LCSNA Real-Time Dashboard',
            page_icon='*',
            layout='wide'
        )

        st.title('Real-Time LCSNA Dashboard')
        st.write(df)
        
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
