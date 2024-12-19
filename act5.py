import streamlit as st
import pandas as pd
import os

# Set the page configuration for the Streamlit app
st.set_page_config(page_title="Dashboard DIY", page_icon="pie", layout="wide")

# Load the dataset
data = pd.read_csv('restaurant. csv') # Replace 'restaurant. csv' with the correct path to your dataset

# Button widget
st.subheader('Displaying Random 5 Rows')
st.caption('Click on the button below to display 5 random rows from the dataset. ')
button = st.button( 'Display random 5 rows')
if button:
st.dataframe(data.sample(5)) # Display 5 random rows from the dataset

# Divider line
st.markdown(' --- ')

# Checkbox widget
st.subheader('Checkbox: st.checkbox')
agree = st.checkbox('I agree to terms and conditions') # Creates a checkbox that returns True or False
st.write('Checkbox status =', agree) # Display the status of the checkbox