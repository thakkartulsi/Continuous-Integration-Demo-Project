import streamlit as st
import requests

st.title('Inspirational Quote Generator ✨')
st.write('Click the button below to get a random inspirational quote!')

# Function to fetch a quote
def get_quote():
    response = requests.get('https://api.quotable.io/random', verify=False)
    if response.status_code == 200:
        quote = response.json()
        return f'{quote['content']}\n\n-*{quote['author']}*'
    else:
        return "Oops! Couldn't fetch a quote. Try again!"

# Button to fetch quote
if st.button('Get a Quote 📜'):
    quote = get_quote()
    st.write(quote)