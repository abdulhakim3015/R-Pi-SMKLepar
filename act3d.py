import streamlit as st
import time # For simulating dynamic updates
import requests


st.title("SMKLEPAR")
st.title("Weather Dashboard")

st.subheader("Load data from openweathermap.org")
user_input = st.text_input("Enter Town Name:")
# The st.text_input() function creates a text box where the user can type their name.
# The text entered by the user is stored in the variable 'user_input'.
api_url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid=ac2d2697871c0160f61dec4ef11b36f9"

try:
    response = requests.get(api_url)
    if response.status_code == 200: # HTTP status codes successfull
        api_data = response.json() #get response in json form
        st.subheader("Raw API Data")
        st.json(api_data, expanded=False)
        weather = api_data['weather'][0]['main' ]
        temperature = api_data['main']['temp'] - 273.15 # Convert Kelvin to Celsius
        

        town_placeholder = st.empty()
        temperature_placeholder = st.empty()
        weather_placeholder = st.empty()
        with town_placeholder:
            st.subheader(f"Current Temperature at {user_input}")
        with temperature_placeholder:
            st.metric(label="Temperature (C)", value=f"{temperature:.1f}")
        with weather_placeholder:
            st.metric(label="Weather", value=f"{weather}")

except Exception as e:
    st.error(f"Error fetching data: {e}")