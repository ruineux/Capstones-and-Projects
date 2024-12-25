import streamlit as st

# Create sample variable to display
get_string = 'Hello World'

# Display sample variable
st.text(f'{get_string}')

# Create html paragraph given set of style #1
apply_textformat1 = f"""
<style>
p.a {{
    font-family:Courier; color:Blue; font-size: 20px;
}}
</style>

<p class='a'> {get_string} </p>
"""
# Create html paragraph given set of style #2
apply_textformat2 = f"""
<style>
p.b {{
    font-family:sans-seriff; color:Green; font-size: 42px;
}}
</style>

<p class='b'> {get_string} </p>
"""

# Display html paragraphs created
st.markdown(apply_textformat1, unsafe_allow_html=True)
st.markdown(apply_textformat2, unsafe_allow_html=True)

# Can be run via cmd
# streamlit run HelloWorld.py