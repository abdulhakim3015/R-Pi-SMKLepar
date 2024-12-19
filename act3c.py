import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Fetch and Display Data from Google Sheets")
# url of google sheet
url = "https://docs.google.com/spreadsheets/d/1iqmm0yPgMBqkrTFkQPTNbT0VZ0bFeYp785zulRGcOdU/edit?usp=sharing"
#establish connection
conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url)
#data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)
# st.dataframe(data, use_container_width=True)
st.caption("Displaying data retrieved from Google Sheets")