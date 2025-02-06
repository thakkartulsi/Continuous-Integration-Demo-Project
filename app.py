"""
Inspirational Quote Generator

This is a Streamlit app that fetches a random inspirational quote
from the Quotable API and displays it to the user.
The user can click a button to retrieve a new quote.
"""
import streamlit as st
import requests


st.title('Inspirational Quote Generator ✨')
st.write('Click the button below to get a random inspirational quote!')


# Function to fetch a quote
def get_quote():
    """
    Fetches a random inspirational quote from the Quotable API.
    If successful, returns the formatted quote and author,
    else returns an error message.
    """
    response = requests.get(
        'https://api.quotable.io/random', verify=False, timeout=5
    )
    if response.status_code == 200:
        quote_data = response.json()
        content = quote_data.get('content', 'No content available.')
        author = quote_data.get('author', 'Unknown author')
        return f"**{content}**\n\n— *{author}*"
    return "Oops! Couldn't fetch a quote. Try again!"


# Button to fetch quote
if st.button('Get a Quote 📜'):
    quote_text = get_quote()
    st.write(quote_text)
