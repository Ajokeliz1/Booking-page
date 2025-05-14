/Include/
/Lib/
/Scripts/
import streamlit as st 
import pandas as pd
import numpy as np
from datetime import datetime

# Page config
st.set_page_config(page_title="Facefield Makeup Booking", page_icon="💄")



# Sidebar fragment function
def fragment_function():
    st.title('Makeup Booking Page')
    st.button("Hello Beautiful!")

with st.sidebar:
    fragment_function()

# Page content
st.header('Facefield Makeup')
st.subheader('Welcome to Facefield Studio, where beauty meets confidence!')
st.write('Kindly fill out the form below')
st.write('--------')

# Initialize data store (simulate a database - you can replace this with actual persistence)
@st.cache_data
def init_data():
    return pd.DataFrame(columns=['Name', 'Phone Number', 'Email', 'Date', 'Time', 'Payment'])

data_store = init_data()

# Booking form
with st.form("booking_form"):
    name = st.text_input('Enter your name')
    phone_number = st.text_input('Enter your Phone Number')
    email = st.text_input('Enter your email')
    date_event = st.date_input('Select your booking date')
    time_event = st.time_input('Select your booking time')

    payment_methods = ['Bank Transfer', 'Cash', 'Others']
    payment = st.selectbox("Select payment method", options=payment_methods)

    submitted = st.form_submit_button('Submit')
    if submitted:
        new_entry = pd.DataFrame([{
            'Name': name,
            'Phone Number': phone_number,
            'Email': email,
            'Date': date_event,
            'Time': time_event,
            'Payment': payment
        }])
        data_store = pd.concat([data_store, new_entry], ignore_index=True)
        st.success('Thanks for your patronage! Your booking has been submitted.')

# Extra interaction
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter Booking Details")

toggle_and_text()

@st.fragment
def filter_and_file():
    cols = st.columns(2)
    cols[0].checkbox("Filter")
    cols[1].file_uploader("Upload Payment Receipt")

filter_and_file()

# Show or download data
st.write('--------')

if st.checkbox("Show collected data"):
    st.dataframe(data_store)

if st.button("Download collected data as CSV"):
    st.download_button(
        label="Download CSV",
        data=data_store.to_csv(index=False).encode('utf-8'),
        file_name='booking.csv',
        mime='text/csv'
    )
