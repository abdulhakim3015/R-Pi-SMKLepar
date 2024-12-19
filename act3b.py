import streamlit as st
import pandas as pd

st.title("Fetch and Display Data from a URL")

# Fetch data
url = 'https://storage.dosm.gov.my/population/population_state.csv'
url_data = pd.read_csv(url)

# Display data
st.subheader("Display Data from URL")
st.dataframe(url_data, use_container_width=True)
st.caption("Displaying data fetched from an online source")