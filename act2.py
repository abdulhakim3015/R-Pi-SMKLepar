import streamlit as st

st.title('This is Title') # Creates a large, bold title
st.header('This is header') # Adds a bold header
st.subheader('This is subheader')
st.write('Displays plain text or any object with st.write()')
st.text('insert text')
st.caption('insert caption')

#Insert a horizontal line for separation
st.divider()

# Displaying Code: Example of a Python code snippet to display in the app
body ="""
import numpy as np
def generate_random(size):
rand = np.random.random(size=size)
return rand
number = generate_random(10)
"""
st.code(body, language='python') # Displays Python code with syntax highlighting

# Example of a mathematical formula rendered with LaTeX
formula = """
a + ar + ar^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} a r^k
"""
st.latex(formula) # Renders the mathematical formula beautifully

# Styled HTML
st.markdown(
"<h3 style='text-align: center; color: red; background-color:lightgrey'>"
"Dashboard Development with Python and Streamlit</h3>",
unsafe_allow_html=True # Allows HTML styling for customization
)
# Links
st.page_link("http://www.google.com", label="Google Link", icon="O")
# Displaying an Image from a URL
st.image("https://news.umpsa.edu.my/sites/default/files/gallery-article/UMPSA%20Solar_0.jpg")

