# Camino Dashboard

A data dashboard from my Camino internship on healthcare access disparities. CAMINO ran a Latino Community Service Needs Assessment (LCSNA), and this Streamlit app was built to display the survey results as a real-time dashboard.

## What it does

`dashboard.py` ("CAMINO LCSNA Real-Time Dashboard"):

- Loads the survey data live from a Google Sheets export URL (the `public_gsheets_url` value in `.streamlit/secrets.toml`), so the dashboard reflects the latest responses without redeploying.
- Displays the raw dataframe on the main page.
- Has a sidebar with three pages: Home, Gender Differences, and Residency Differences, intended for slicing the needs-assessment results by demographics.

This is an early version: the Home page still carries placeholder copy and the Gender/Residency pages are empty stubs, so treat it as a work-in-progress dashboard scaffold rather than a finished product.

## Data

The survey data lives in Google Sheets (private to the internship), not in this repo. The app reads it at runtime through the secrets URL.

## Install and run

```bash
git clone https://github.com/suhasaitham22/camino-dashboard.git
cd camino-dashboard
pip install -r requirements.txt
```

Add the sheet URL to `.streamlit/secrets.toml`:

```toml
public_gsheets_url = "https://docs.google.com/spreadsheets/d/<id>"
```

Then:

```bash
streamlit run dashboard.py
```

## Tech stack

Streamlit, pandas, NumPy, Plotly, requests.
