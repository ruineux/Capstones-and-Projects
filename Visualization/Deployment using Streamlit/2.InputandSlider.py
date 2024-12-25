import streamlit as st

# Create streamlit object text input with default value
variable_output = st.text_input("Enter some text", value="Change this to display different text")

# Create streamlit object slider to adjust font size
font_size = st.slider("Enter a font size", 1, 300, value=30)

# Create html utilizing the two parameters
html_str = f"""
<style>
p.a {{
  font:bold; font-size:{font_size}px; font-family:Arial;
}}
</style>
<p class="a">{variable_output}</p>
"""

st.markdown(html_str, unsafe_allow_html=True)

# Can be run via cmd
# streamlit run InputandSlider.py