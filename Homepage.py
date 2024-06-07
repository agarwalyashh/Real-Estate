import streamlit as st
import pandas as pd
st.set_page_config(
    page_title='Gurgaon'
)
st.title("Gurgaon's Real Estate App")
st.header('Features of this application-')
st.write('1. Price Predictor Module : You can feed in your requirements and get an estimate of your flat\'s price')
st.write('2. Explore the Analytics module to gain visual representation of Real Estate Market in Gurgaon')
st.write('3. Based on your requirements and choices, the Recommender module recommends similar properties which might '
         ' be of your interest')
st.sidebar.success("Select a demo above")

