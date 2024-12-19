import streamlit as st

st.title("my first dashbord app")

st.title("Hello, Welcome to my first dashboard app!")

User_input = st.text_input("hakim")

st.write(f"Congratulations, {user_input}! This is your dashboard")